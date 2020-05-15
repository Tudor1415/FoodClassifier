import os

import numpy as np
from PIL import Image


# Resizing the images in all the folders of all the directories

for dir in os.listdir("images"):
    for imagePath in os.listdir(dir):
        img = Image.open(imagePath)