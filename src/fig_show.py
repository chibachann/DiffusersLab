import matplotlib.pyplot as plt

def fig_show(dataset):
    fig, axs = plt.subplots(1, 4, figsize=(16, 4))
    for i, image in enumerate(dataset[:4]["image"]):
        axs[i].imshow(image)
        axs[i].set_axis_off()
    plt.savefig("fig_show.png")
    plt.close(fig)
