from datasets import load_dataset
from config import config

def LoadDataset():
    config.dataset_name = "huggan/smithsonian_butterflies_subset"
    dataset = load_dataset(config.dataset_name, split="train")
    return dataset

