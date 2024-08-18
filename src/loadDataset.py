from datasets import load_dataset
from config import config

def LoadDataset(dataset_name):
    config.dataset_name = dataset_name
    dataset = load_dataset(config.dataset_name, split="train")
    return dataset

