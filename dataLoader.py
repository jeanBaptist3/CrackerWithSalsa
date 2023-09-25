import csv
import base64
from datasets import load_dataset, Dataset

from tokenizers import Tokenizer

tokenizer = Tokenizer.from_file(path='tokenizer_stuff/custom_tokenizer_wordpiece.json')

# Initialize a list to store your processed data
processed_data = []


def load_csv(path):
    return load_dataset("csv", data_files=path)


def prepare_data(data):
    tokenized_input = tokenize_function(data['train'])
    tokenized_output = tokenize_out(data['train'])

    train_data = Dataset.from_dict(
        {
            "input_ids": list(map(get_ids, tokenized_input)),
            "attention_mask": list(map(get_attention, tokenized_input)),
            "labels": list(map(get_ids, tokenized_output)),
        }
    )
    full_dataset = train_data.train_test_split(test_size=1 / 11)

    return full_dataset


def tokenize_function(example):
    return tokenizer.encode_batch(example['block_and_nonce'])


def tokenize_out(example):
    return tokenizer.encode_batch(example['next_block'])


def get_attention(encoding):
    return encoding.attention_mask


def get_ids(encoding):
    return encoding.ids
