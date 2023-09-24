import struct
from datasets import Dataset
from tokenizers import Tokenizer, trainers, pre_tokenizers, decoders
from tokenizers.models import WordLevel

min_int = -2**16
max_int = 2**16-1

def gen():
    for i in range(min_int, max_int) :
        yield {'byte' : struct.pack('I',i & 0xFFFFFFFF).hex()}

tokenizer = Tokenizer(WordLevel())

# Define a custom pre-tokenizer with rules to split on punctuation and recognize custom tokens
tokenizer1 = pre_tokenizers.WhitespaceSplit()
tokenizer2 = pre_tokenizers.CharDelimiterSplit(',')
pre_tokenizer = pre_tokenizers.Sequence([tokenizer1,tokenizer2])

tokenizer.pre_tokenizer = pre_tokenizer

# Define a custom decoder
decoder = decoders.ByteLevel()
tokenizer.decoder = decoder

# Train the tokenizer
trainer = trainers.WordLevelTrainer(vocab_size= 2**32 + 2,show_progress = True,special_tokens=["[PAD]", "[CLS]", "[SEP]", "[MASK]", "[UNK]", "[NONC1]", "[NONC2]"])
tokenizer.train_from_iterator(Dataset.from_generator(gen), trainer=trainer)


# Save the trained tokenizer to a file
tokenizer.save("tokenizer_stuff/custom_tokenizer.json")

print("Saved Tokenizer")