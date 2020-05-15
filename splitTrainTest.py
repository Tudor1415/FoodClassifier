import os
import random as rd

from PIL import Image

# Spliting the images in all the folders of all the directories in 20% test and 80% train
sizes = []
os.mkdir("Preprocessed/train")
os.mkdir("Preprocessed/test")
for dir in os.listdir("Preprocessed/images/"):
    if dir not in os.listdir('Preprocessed/train/'):
        os.mkdir(f"Preprocessed/train/{dir}")
    if dir not in os.listdir('Preprocessed/test/'):
        os.mkdir(f"Preprocessed/test/{dir}")
    for imagePath in os.listdir("Dataset/images/"+dir):
        if rd.randint(0,100) < 20:
            os.rename(f"Preprocessed/images/{dir}/{imagePath}", f"Preprocessed/train/{dir}/{imagePath}")
        else:
            os.rename(f"Preprocessed/images/{dir}/{imagePath}", f"Preprocessed/test/{dir}/{imagePath}")

os.remove("Preprocessed/images")