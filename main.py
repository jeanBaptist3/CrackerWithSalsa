import dataCreation
#from torch.utils.data import DataLoader
from tqdm.auto import tqdm
import dataLoader
from transformers import AutoModel
from tokenizers import Tokenizer


tokenizer = Tokenizer.from_file(path='tokenizer_stuff/custom_tokenizer_wordpiece.json')
print(tokenizer.get_vocab_size())
model = AutoModel.from_pretrained("google/flan-t5-small")
def main() :
    #dataCreation.create_data(2,1,2)
    raw_data = dataLoader.load_csv("data/data_dump.csv")

    split_data = dataLoader.prepare_data(raw_data)
    print(raw_data)

    #model = AutoModel.from_pretrained("google/flan-t5-small")



if __name__ =="__main__":
    checkpoint = "google/flan-t5-small"

    main()

