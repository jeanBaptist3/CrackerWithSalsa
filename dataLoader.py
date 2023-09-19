import csv
import base64

# Initialize a list to store your processed data
processed_data = []

# Open the CSV file for reading
with open('data/data_dump.csv', 'r', encoding='UTF8', newline='') as csv_file:
    reader = csv.reader(csv_file)
    # Skip the header row
    next(reader, None)

    for row in reader:
        if len(row) < 1:
            # Handle empty lines or rows with insufficient data
            continue

        # Extract data from the CSV row
        ciphertext_hex, nonce_hex = row
        ciphertext = bytes.fromhex(ciphertext_hex)
        nonce = bytes.fromhex(nonce_hex)

        # Store the processed data in a suitable data structure
        processed_data.append({
            'ciphertext': ciphertext,
            'nonce': nonce
        })

# Now, processed_data contains the binary data in a usable format
# You can access and manipulate it as needed
for item in processed_data:
    print(f'Ciphertext: {item["ciphertext"]}')
    print(f'Nonce: {item["nonce"]}')