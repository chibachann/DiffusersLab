from torchvision import transforms
import torch

from src.loadDataset import LoadDataset
from src.fig_show import fig_show, transformed_fig
from src.transform import transform
from src.train_dataloader import Train_Dataloader
from src.process_image import process_sample_image
from src.train_step import setup_training
from src.noise_scheduler import noise_image
import train

def main():
    dataset_name = "huggan/smithsonian_butterflies_subset"
    dataset = LoadDataset(dataset_name)
    print(dataset)
    fig_show(dataset)
    dataset.set_transform(transform)
    transformed_fig(dataset)
    train_dataloader = Train_Dataloader(dataset)

    sample_image = dataset[0]['images'].unsqueeze(0)
    noise = torch.randn(sample_image.shape)
    timesteps = torch.LongTensor([50])
    noisy_image = noise_image(sample_image, noise, timesteps)

    # Process the sample image and save it
    process_sample_image(sample_image, noisy_image)
    print("Processed image has been saved as 'processed_image.png'")

    # Compute the loss
    loss, optimizer, lr_scheduler = setup_training(noisy_image, noise, timesteps, train_dataloader)

    # Train the model
    train.train(optimizer, train_dataloader, lr_scheduler)

if __name__ == "__main__":
    main()
