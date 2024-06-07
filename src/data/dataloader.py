from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
from torch.utils.data import Dataset, DataLoader
import albumentations as A
from albumentations.pytorch import ToTensorV2

class CustomDataset(Dataset):
    def __init__(self, folder_path, transform=None):
        self.folder_path = folder_path
        self.transform = transform
        self.image_files = [f for f in os.listdir(folder_path) if f.endswith(".png") or f.endswith(".jpg")]

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_path = os.path.join(self.folder_path, self.image_files[idx])
        image = Image.open(img_path)
        width, height = image.size
        half_width = width // 2
        left_image = image.crop((0, 0, half_width, height))
        right_image = image.crop((half_width, 0, width, height))
        if self.transform:

            transformed = self.transform(image=np.array(left_image), image0=np.array(right_image))
            left_image, right_image = transformed['image'], transformed['image0']

        return left_image, right_image

folder_path = '/data/train'

# https://albumentations.ai/docs/api_reference/augmentations/
transform = A.Compose([
    A.ColorJitter(p=0.3),
    A.Resize(256, 256),
    A.Rotate(limit=40),
    ToTensorV2(),
], additional_targets = {'image0': 'image'})

dataset = CustomDataset(folder_path, transform=transform)

dataloader = DataLoader(dataset, batch_size=10, shuffle=False)

def show_images(left_image, right_image):

    for i, (left_img, right_img) in enumerate(zip(left_image, right_image)):
        fig = plt.figure(figsize=(5, 5))
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        left_img = left_img.permute(1, 2, 0)
        right_img = right_img.permute(1, 2, 0)
        ax1.imshow(left_img)
        ax2.imshow(right_img)


for images in dataloader:
    show_images(images[0], images[1])
    break