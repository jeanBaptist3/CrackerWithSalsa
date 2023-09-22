import struct
from datasets import Dataset
from time import time


timestart = time()
# Function to generate and yield 32-bit binary strings as bytes
def generate_binary_strings(min_int, max_int):
    for i in range(min_int, max_int + 1):
        binary_string = struct.pack('I', i & 0xFFFFFFFF)
        yield binary_string

min_int = -2**31  # Minimum 32-bit integer
max_int = 2**31 -1 # Maximum 32-bit integer
output_directory = "data"  # Specify your output directory

data_generator = generate_binary_strings(min_int, max_int)

# Create a list to store the generated binary strings
binary_strings = list(data_generator)

# Create a Dataset from the list of binary strings
dataset = Dataset.from_dict({"byte": binary_strings})

# Save the dataset to disk in your desired format (e.g., Arrow)
dataset.save_to_disk(f"{output_directory}/binary_strings.arrow", storage_options={"compress": "gzip"})

print("--- % seconds ---" % str(time()-timestart))