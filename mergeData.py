import os
import shutil

from PIL import Image

shutil.rmtree("Dataset")
for dir in os.listdir("Augmented/train/"):
    for imagePath in os.listdir("Augmented/train/"+dir):
        os.rename(f"Augmented/train/{dir}/{imagePath}" , f"Preprocessed/train/{dir}/{imagePath}")
