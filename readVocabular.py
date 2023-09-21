from datasets import load_from_disk
from transformers import AutoTokenizer, AutoModel
from tokenizers.pre_tokenizers import Punctuation
import struct

print("klappt")
# Load the dataset containing binary representations of 32-bit integers
dataset = load_from_disk("32_bit_integers_dataset_compressed")

# Function to convert binary strings to integers and then to the desired string format
def binary_to_string(binary_str):
    integer_value = struct.unpack('i', bytes.fromhex(binary_str))[0]  # Convert binary string to integer
    return format(integer_value, '032b')  # Convert integer to a 32-bit binary string without '0b'

# Apply the conversion function to the dataset
dataset = dataset.map(lambda example: {'data': binary_to_string(example['data'])}, batched=True)

# Train a tokenizer using the transformed dataset
from transformers import AutoTokenizer

# T5Model and T5TokenizerFast

tokenizer = AutoTokenizer.from_pretrained("t5-small")(special_tokens =["[NONC1]","[NONC2]"])
model = AutoModel.from_pretrained("t5-small")

# define preTokenizer

tokenizer.pre_tokenizer = Punctuation()

# Tokenize the data
tokenized_data = dataset.map(lambda examples: tokenizer(examples['data'], truncation=True, padding='max_length', max_length=128), batched=True)

# Now, you can use 'tokenized_data' to train a model or perform other NLP tasks with Hugging Face Transformers.