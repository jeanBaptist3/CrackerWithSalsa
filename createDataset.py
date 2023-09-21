import struct
import time
from datasets import Dataset

start_time = time.time();
# Define the batch size
batch_size = 2**8  # You can adjust this to your preferred batch size

min_int = 0 # Minimum 32-bit integer
max_int = 2**24  # Maximum 32-bit integer

# Generate data in batches
data_batches = []
batch = []

for i in range(min_int, max_int):
    batch.append({"byte": struct.pack('i', i)})

    # Check if the batch is full
    if len(batch) == batch_size:
        data_batches.append(batch)
        batch = []

# If there are remaining items in the last batch, add it
if batch:
    data_batches.append(batch)

# Create a dataset from the list of data batches
dataset = Dataset.from_dict({"data": data_batches})

# Save the dataset to disk with gzip compression
dataset.save_to_disk("allStrings", storage_options={"compress": "gzip"})

print("Dataset with compression created and saved.")
print("--- % seconds ----" % (time.time() - start_time))