import numpy as np
import csv
from datasets import load_dataset
from Crypto.Cipher import ChaCha20 as Cha
from Crypto.Random import get_random_bytes
from base64 import b64encode
from base64 import b64decode
from transformers import T5TokenizerFast

#this is the plaintext, 256*blocks bit only 0, so the encrytion will yield only the stream from ChaCha


def create_data(generated_blocks, prediction_blocks) :
    prefix = "predict the next 512 bit "
    plaintext = b''
    train_size = 90000
    test_size = 10000
    val_size = 10000
    full_size = val_size+ test_size+ train_size


    gen_blocks = generated_blocks
    pred_blocks = prediction_blocks
    blocks = gen_blocks + pred_blocks
    for i in range (0,blocks*64) :
        plaintext = plaintext + b'\x00'


    """
    These are the arrays consisting of the keys to train and their ciphertexts and nonces
    """
    keys = []
    ciphers = []
    ciphetexts = []
    nonces = []
    data = []
    plaintexts = []
    number_of_keys = 1
    counter = 0
    cipher = Cha.new(key = get_random_bytes(32))
    for i in range(0, full_size) :
        if (i % (full_size / number_of_keys) == 0):
            keys.append(get_random_bytes(32))
            counter = counter + 1
        ciphers.append(Cha.new(key=keys[counter-1]))
        ciphers[i].seek(0)
        ciphetext = ciphers[i].encrypt(plaintext)
        ciphetexts.append(ciphetext)
        nonce = ciphers[i].nonce
        ciphetext_bits = ''.join(format(byte,'08b') for byte in ciphetext)
        nonce_bits = ''.join(format(byte, '08b') for byte in nonce)
        nonces.append(nonce)
        pretokenized_string = ciphetext_bits
        for j in range(0,blocks*16) :
            pretokenized_string = pretokenized_string[:blocks*512-j*32] + ',' +pretokenized_string[blocks*512-j*32:]
        
        data.append([ pretokenized_string[33*32:] + ',[NONC1]' +nonce_bits[:32] +',[NONC2]' + nonce_bits[32:] , pretokenized_string[:32*33] ])

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
    header = ['block_and_nonce','next_block']

    print(b64encode(plaintext).decode('utf-8') + "test")
    with open(r'data/data_dump.csv', 'w', encoding='UTF8',newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(header)
        for text in data :
            writer.writerow(text)


