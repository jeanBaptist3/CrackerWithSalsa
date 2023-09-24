import struct
from datasets import Dataset
from time import time
from tokenizers import Tokenizer, trainers, pre_tokenizers, decoders
from tokenizers.models import WordLevel

timestart = time()
# Function to generate and yield 32-bit binary strings as bytes
def generate_binary_strings(min_int, max_int):
    for i in range(min_int, max_int + 1):
        binary_string = struct.pack('I', i & 0xFFFF).hex()
        yield binary_string

min_int = -2**16 # Minimum 32-bit integer
max_int = 2**16 -1 # Maximum 32-bit integer
output_directory = "data"  # Specify your output directory


#dataset = Dataset.from_dict({"byte": binary_strings})
#dataset.save_to_disk(f"{output_directory}/binary_strings_new.arrow", storage_options={"compress": "gzip"})

# initializing new Tokenizer
tokenizer = Tokenizer(WordLevel())

#pre_tokenizers
tokenizer1 = pre_tokenizers.WhitespaceSplit()
tokenizer2 = pre_tokenizers.CharDelimiterSplit(',')
pre_tokenizer = pre_tokenizers.Sequence([tokenizer1,tokenizer2])

tokenizer.pre_tokenizer = pre_tokenizer

#decoder
decoder = decoders.ByteLevel()
tokenizer.decoder = decoder



# Train the tokenizer
trainer = trainers.WordLevelTrainer(vocab_size= 2**16 + 37,show_progress = True,special_tokens=["[PAD]", "[CLS]", "[SEP]", "[MASK]", "[UNK]", "[NONC1]", "[NONC2]", "[NONC3]","[NONC0]"])
tokenizer.train_from_iterator(generate_binary_strings(min_int, max_int), trainer=trainer)


# Save the trained tokenizer to a file
tokenizer.save("tokenizer_stuff/custom_tokenizer.json")

print("Saved Tokenizer")

print("--- % seconds ---" % str(time()-timestart))