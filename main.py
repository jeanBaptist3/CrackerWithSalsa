import dataCreation
import dataLoader
from transformers import T5TokenizerFast

def main() :
    dataCreation.create_data(2,1)
    raw_data = dataLoader.load_csv("data/data_dump.csv")
    split_data = dataLoader.prepare_data(raw_data)
    print("begin tokenization")
    tokenized_data = split_data.map(tokenize_function, batched=True)
    print("fertig")
    tokenized_data = tokenized_data.remove_columns(['block_and_nonce','next_block'])
    toke


def tokenize_function(example) :
    return tokenizer(example['block_and_nonce'], example['next_block'], truncation=True)

if __name__ =="__main__":
    checkpoint = "google/flan-t5-small"
    tokenizer = T5TokenizerFast.from_pretrained(checkpoint)
    main()

