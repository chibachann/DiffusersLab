import torch
from config import config

def Train_Dataloader(dataset):
    train_dataloader = torch.utils.data.DataLoader(dataset, batch_size=config.train_batch_size, shuffle=True)
    return train_dataloader
