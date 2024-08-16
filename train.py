from accelerate import notebook_launcher
from src.training_loop import train_loop
from config import config
from src.noise_scheduler import noise_scheduler
from models.model import model

def train(optimizer, train_dataloader, lr_scheduler):
    args = (config, model, noise_scheduler, optimizer, train_dataloader, lr_scheduler)

    notebook_launcher(train_loop, args, num_processes=1)
