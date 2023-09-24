import dataCreation
from datasets import Dataset
import dataLoader
from tokenizers import Tokenizer
tokenizer = Tokenizer.from_file(path='tokenizer_stuff/custom_tokenizer.json')
tokenizer.encode('abcd')
def main() :
    #dataCreation.create_data(2,1,2)
    raw_data = dataLoader.load_csv("data/data_dump.csv")
    split_data = dataLoader.prepare_data(raw_data)
    print("begin tokenization")
    print(type(split_data['train']))
    print("fertig")
    tokenized_data = split_data['train'].map(tokenize_function, batched= True)


def tokenize_function(example):
    return {'train' : tokenizer.encode_batch(example['block_and_nonce'])}


if __name__ =="__main__":
    checkpoint = "google/flan-t5-small"

    main()

