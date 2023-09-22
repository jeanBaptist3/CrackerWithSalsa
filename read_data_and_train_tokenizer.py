import struct
from datasets import Dataset
from tokenizers import Tokenizer, trainers, pre_tokenizers, decoders
from tokenizers.models import WordLevel
# Load the dataset from the saved disk location
fulldata = []


#function to convert the bytes to binary strings
def binary_to_bit_string(binary_data):
    # Unpack as a 4-byte integer using 'i' format
    byte_value = struct.unpack('i', binary_data)[0]
    # Convert to binary and pad to 32 bits
    if byte_value < 0:
        # If the value is negative, convert to a 32-bit binary string with the sign bit
        bit_string = bin(byte_value & 0xFFFFFFFF)[2:]
    else:
        # If the value is non-negative, convert to a 32-bit binary string without the sign bit
        bit_string = bin(byte_value)[2:].zfill(32)
    return bit_string



dataset = Dataset.load_from_disk(f"data/binary_strings.arrow")
for integer in dataset["byte"] :
    fulldata.append(binary_to_bit_string(integer))


# Initialize a custom tokenizer
tokenizer = Tokenizer(WordLevel())

# Define a custom pre-tokenizer with rules to split on punctuation and recognize custom tokens
tokenizer1 = pre_tokenizers.WhitespaceSplit()
tokenizer2 = pre_tokenizers.CharDelimiterSplit(',')
pre_tokenizer = pre_tokenizers.Sequence([tokenizer1,tokenizer2])

tokenizer.pre_tokenizer = pre_tokenizer

# Define a custom decoder
decoder = decoders.ByteLevel()
tokenizer.decoder = decoder


training_data = fulldata

# Train the tokenizer
trainer = trainers.WordLevelTrainer(vocab_size= 2**32 + 2,show_progress = True,special_tokens=["[PAD]", "[CLS]", "[SEP]", "[MASK]", "[UNK]", "[NONC1]", "[NONC2]"])
tokenizer.train_from_iterator(training_data, trainer=trainer)


# Save the trained tokenizer to a file
tokenizer.save("tokenizer_stuff/custom_tokenizer.json")

print("Saved Tokenizer")