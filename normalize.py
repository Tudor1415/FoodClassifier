import os

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Resizing the images in all the folders of all the directories
sizes = []
for dir in os.listdir("Dataset/images/"):
    if dir not in os.listdir('Preprocessed/images/'):
        os.mkdir(f"Preprocessed/images/{dir}")
    for imagePath in os.listdir("Dataset/images/"+dir):
        img = Image.open(f"Dataset/images/{dir}/{imagePath}")
        print(img.size)
        if img.size != (80,80):
            sizes.append(img.size)
        
        resized = img.resize((100,100), Image.ANTIALIAS)
        resized.save(f"Preprocessed/images/{dir}/{imagePath}")

print(min(sizes))

