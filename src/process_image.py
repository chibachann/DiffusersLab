import torch
from PIL import Image
from models.model import model


def process_sample_image(sample_image, noisy_image):
    print('Input shape:', sample_image.shape)
    print('Output shape:', model(sample_image, timestep=0).sample.shape)
    
    processed_image = Image.fromarray(((noisy_image.permute(0, 2, 3, 1) + 1.0) * 127.5).type(torch.uint8).numpy()[0])
    processed_image.save("processed_image.png")
