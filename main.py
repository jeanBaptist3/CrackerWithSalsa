import dataCreation
from datasets import Dataset
import dataLoader
from tokenizers import Tokenizer
tokenizer = Tokenizer.from_file(path='tokenizer_stuff/custom_tokenizer_wordpiece.json')
print(tokenizer.get_vocab_size())
def main() :
    #dataCreation.create_data(2,1,2)
    raw_data = dataLoader.load_csv("data/data_dump.csv")
    split_data = dataLoader.prepare_data(raw_data)
    print("begin tokenization")
    print(type(split_data['train']))
    print("fertig")
    test = tokenizer.encode_batch(['ff00', '00ff'])
    print(test[1])
    tokenized_data = tokenize_function(split_data['train'])
    print(type(tokenized_data))

def tokenize_function(example):
    return tokenizer.encode_batch(example['block_and_nonce'])


if __name__ =="__main__":
    checkpoint = "google/flan-t5-small"

    main()

