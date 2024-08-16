from diffusers import DDPMScheduler


noise_scheduler = DDPMScheduler(num_train_timesteps=1000)


def noise_image(sample_image, noise, timesteps):
    noisy_image = noise_scheduler.add_noise(sample_image, noise, timesteps)
    return noisy_image
