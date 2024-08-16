import torch
import torch.nn.functional as F
from transformers import get_cosine_schedule_with_warmup
from models.model import model
from config import config

def setup_training(noisy_image, noise, timesteps, train_dataloader):
    noise_pred = model(noisy_image, timesteps).sample
    loss = F.mse_loss(noise_pred, noise)
    optimizer = torch.optim.AdamW(model.parameters(), lr=config.learning_rate)

    lr_scheduler = get_cosine_schedule_with_warmup(
        optimizer=optimizer,
        num_warmup_steps=config.lr_warmup_steps,
        num_training_steps=(len(train_dataloader) * config.num_epochs),
    )
    return loss, optimizer, lr_scheduler
