import csv

from Crypto.Cipher import ChaCha20 as Cha
from Crypto.Random import get_random_bytes
from base64 import b64encode
from base64 import b64decode
import numpy as np
import plotly.express as px

#This Code is the C/C++ implementation of the ChaCha Chiffre, invented by Daniel J. Bernstein, from wikipedia : https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant, converted into python


#this function returns a bit String given bytes
def toBitString(data) :
    return ''.join(format(byte,'08b') for byte in data)

#this is the plaintext, 256*blocks bit only 0, so the encrytion will yield only the stream from ChaCha


plaintext = b''
plaintextTwo = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
plaintextthree = b''
batchSize = 1000;
testsize = 10000;
hexa = plaintextTwo.hex()

blocks = 6
for i in range (0,blocks) :
    plaintext = plaintext + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'


"""
These are the arrays consisting of the keys to train and their ciphertexts and nonces
"""
keys = []
ciphers = []
ciphetexts = []
nonces = []
dictionary = []
plaintexts = []
cipher = Cha.new(key = get_random_bytes(32))
for i in range(0, testsize) :
    keys.append(get_random_bytes(32))
    ciphers.append(Cha.new(key=keys[i]))
    ciphers[i].seek(0)
    ciphetext = ciphers[i].encrypt(plaintext)
    ciphetexts.append(ciphetext)
    nonce = ciphers[i].nonce
    ciphetext_bits = ''.join(format(byte,'08b') for byte in ciphetext)
    nonce_bits = ''.join(format(byte, '08b') for byte in nonce)
    nonces.append(nonce)
    dictionary.append([ciphetext_bits, nonce_bits])

"""
This is for testing the correct encoding and decoding 

ciphersnew = []
plaintextTests = []
for i in range(0, testsize) :
    nonce = b64decode(nonces[i])
    ciphertext = b64decode(ciphetexts[i])
    ciphersnew.append(Cha.new(key=keys[i], nonce=nonce))
    plaintextTest = ciphersnew[i].decrypt(ciphertext)
    plaintextTests.append(plaintextTest)
    print(plaintextTest

cipherTwo =b64encode(ciphers[0].encrypt(plaintextTwo)).decode('utf-8')
print(cipherTwo)

Neural Net consisting of 570 Input Nodes and 2 hidden layer with 1024 Nodes and 512 output layer => 2 Million Parameters
"""
header = ['block','nonce']
#print(plaintextTest)
print(hexa)
print(b64encode(plaintext).decode('utf-8') + "test")
with open(r'data/data_dump.csv', 'w', encoding='UTF8',newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(header)
    for text in dictionary :
        writer.writerow(text)
print("fertig")
length = len(plaintext)

print(length)






