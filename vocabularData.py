import gzip
import struct

# Define the range of 32-bit integers
min_int = 0  # Minimum 32-bit integer
max_int = 2**31 - 1  # Maximum 32-bit integer

# File name
output_file_name = "32_bit_integers.bin.gz"

# Open a gzip-compressed binary file for writing
with gzip.open(output_file_name, "wb") as file:
    # Generate and write all 32-bit integers as binary data
    for i in range(min_int, max_int + 1):
        binary_data = struct.pack('i', i)  # Pack the integer as a 4-byte binary data
        file.write(binary_data)

print(f"All 32-bit integers have been generated and saved to '{output_file_name}' (gzipped binary).")
