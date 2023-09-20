import gzip
import struct

def padto32BitString(number) :
    paddedString = number
    while len(paddedString) < 32 :
            paddedString = '0' + paddedString
    return paddedString
# File name
input_file_name = "32_bit_integers.bin.gz"

# Number of integers to extract (change this to the desired value)
n = 10

# Open the gzipped binary file for reading
with gzip.open(input_file_name, "rb") as file:
    integers = []

    # Read and unpack the first 'n' integers
    for _ in range(n):
        binary_data = file.read(4)  # Read 4 bytes (32 bits)
        if not binary_data:
            break  # Reached the end of the file
        integer = struct.unpack('i', binary_data)[0]  # Unpack as a 32-bit integer
        integers.append(bin(integer)[2:])

    integers = list(map(padto32BitString,integers))
print(f"The first {n} 32-bit integers from '{input_file_name}' are: {integers}")
