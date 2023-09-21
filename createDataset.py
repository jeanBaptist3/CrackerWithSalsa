import struct
import time
import concurrent.futures
from datasets import Dataset

#start_time = time.time();


# batch size for memory regulation
batch_size = 2**21

min_int = -2**31 # Minimum 32-bit integer
max_int = 2**31 -1 # Maximum 32-bit integer
output_directory = "data"

# Function to generate a batch of data
def generate_and_save_batch(start, end, filename):
    batch = []
    for i in range(start, end):
        batch.append({"byte": struct.pack('i', i)})

        # Check if the batch is full
        if len(batch) == batch_size:
            dataset = Dataset.from_dict({"data": batch})
            dataset.save_to_disk(f"{output_directory}/{filename}", storage_options={"compress": "gzip"})
            batch = []

    # Save any remaining data in the last batch
    if batch:
        dataset = Dataset.from_dict({"data": batch})
        dataset.save_to_disk(f"{output_directory}/{filename}", storage_options={"compress": "gzip"})

# Define the number of parallel workers (adjust as needed)
num_workers = 32

# Create a ThreadPoolExecutor with the specified number of workers
with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
    futures = []

    # Divide the range into chunks for parallel processing
    chunk_size = (max_int - min_int) // num_workers

    for i in range(min_int, max_int, chunk_size):
        start = i
        end = min(i + chunk_size, max_int)
        filename = f"allStrings_partial_{start}_{end}.arrow"
        futures.append(executor.submit(generate_and_save_batch, start, end, filename))

# Wait for all tasks to complete
concurrent.futures.wait(futures)

print("Dataset with compression created and saved in parallel batches.")


#print("--- % seconds ----" % (time.time() - start_time))