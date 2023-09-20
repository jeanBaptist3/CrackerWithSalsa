import csv
import base64
from datasets import load_dataset


# Initialize a list to store your processed data
processed_data = []

def load_csv(path) :
    return load_dataset("csv",data_files = path)

def prepare_data(data):
    adjusted_dataset = data['train'].train_test_split(train_size=10/11, seed=1729)
    full_dataset = adjusted_dataset['train'].train_test_split(train_size=9/10, seed =2020)
    full_dataset['validation'] = adjusted_dataset.pop('test')
    return full_dataset