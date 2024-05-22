import os
import re

import torch
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms


class MyDataset(Dataset):
    def __init__(self, root_path, train, transform=None):
        self.root_path = root_path
        self.transform = transform
        if train:
            self.root_path = os.path.join(self.root_path, 'training')
        else:
            self.root_path = os.path.join(self.root_path, 'testing')

        self.img_paths = []
        self.labels = []
        for label_path in os.listdir(self.root_path):
            img_path = os.path.join(self.root_path, label_path)
            if os.path.isdir(img_path):
                for img in os.listdir(img_path):
                    # 使用正则获取图片名称中的信息
                    match = re.search(r'_(\d+)', img)
                    label = match.group(1)
                    # print(f'label: {label}')
                    pre_img_path = os.path.join(img_path, img)
                    self.img_paths.append(pre_img_path)
                    self.labels.append(label)

    def __len__(self):
        return len(self.img_paths)

    def __getitem__(self, index):
        img = self.img_paths[index]
        label = self.labels[index]
        img = Image.open(img)
        if self.transform is not None:
            img = self.transform(img)
        label = int(label)
        label = torch.tensor(label)
        return img, label


if __name__ == '__main__':
    root_dir = '../datasets/mnist_png'
    my_dataset = MyDataset(root_dir, train=True, transform=transforms.ToTensor())
    img, label = my_dataset[0]
    print(f'img: {img}, label: {label}')

