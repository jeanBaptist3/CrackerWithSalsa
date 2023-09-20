from datasets import Dataset
import struct
import gzip
import time

# Define the range of 32-bit integers
min_int = -2**31  # Minimum 32-bit integer
max_int = 2**31 - 1  # Maximum 32-bit integer

start_time = time.time()
# Define a generator function to produce binary data one item at a time
def generate_binary_data():
    for i in range(min_int, max_int + 1):
        yield struct.pack('i', i)

print("--- %s seconds ---" % (time.time() - start_time))
# Create a dataset using the generator
dataset = Dataset.from_generator(generate_binary_data, output_signature={"data": "bytes"})

# Specify a compression option when saving to disk
dataset.save_to_disk("32_bit_integers_dataset_compressed", storage_options={"compress": "gzip"})

print("Dataset with compression created and saved.")

