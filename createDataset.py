import struct
from datasets import Dataset
from time import time
from tokenizers import Tokenizer, trainers, pre_tokenizers, decoders
from tokenizers.models import WordLevel

timestart = time()
# Function to generate and yield 32-bit binary strings as bytes
def generate_binary_strings(min_int, max_int):
    for i in range(min_int, max_int + 1):
        binary_string = struct.pack('I', i & 0xFFFFFFFF)
        yield binary_string

min_int = 0 # Minimum 32-bit integer
max_int = 2**17 -1 # Maximum 32-bit integer
output_directory = "data"  # Specify your output directory

data_generator = generate_binary_strings(min_int, max_int)

# Create a list to store the generated binary strings


# Create a Dataset from the list of binary strings
#dataset = Dataset.from_dict({"byte": binary_strings})

# Save the dataset to disk in your desired format (e.g., Arrow)
#dataset.save_to_disk(f"{output_directory}/binary_strings_new.arrow", storage_options={"compress": "gzip"})

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


training_data = binary_strings

# Train the tokenizer
trainer = trainers.WordLevelTrainer(vocab_size= 2**32 + 2,show_progress = True,special_tokens=["[PAD]", "[CLS]", "[SEP]", "[MASK]", "[UNK]", "[NONC1]", "[NONC2]"])
tokenizer.train_from_iterator(training_data, trainer=trainer)


# Save the trained tokenizer to a file
tokenizer.save("tokenizer_stuff/custom_tokenizer.json")

print("Saved Tokenizer")

print("--- % seconds ---" % str(time()-timestart))