from torchvision import transforms

from loadDataset import LoadDataset
from fig_show import fig_show
from transform import transform, transformed_fig

def main():
    dataset = LoadDataset()
    print(dataset)
    fig_show(dataset)
    dataset.set_transform(transform)
    transformed_fig(dataset)

if __name__ == "__main__":
    main()
