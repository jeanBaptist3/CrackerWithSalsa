from datasets import Dataset
import struct
import gzip

# Define the range of 32-bit integers
min_int = -2**31  # Minimum 32-bit integer
max_int = 2**31 - 1  # Maximum 32-bit integer

# Generate a list of 32-bit integers
integers = list(range(min_int, max_int + 1))

# Convert integers to bytes
byte_data = [struct.pack('i', i) for i in integers]

# Create a dataset
dataset = Dataset.from_dict({"data": byte_data})

# Specify a compression option when saving to disk
dataset.save_to_disk("32_bit_integers_dataset_compressed", storage_options={"compress": "gzip"})

print("Dataset with compression created and saved.")
