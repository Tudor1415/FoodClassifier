import os
import pandas as pd

train = pd.DataFrame()
test = pd.DataFrame()

for d in ["Preprocessed/train", "Preprocessed/test"]:
    Lables = []; Path = []
    for dir in os.listdir(d):
        for imagePath in os.listdir(f"{d}/{dir}/"):
            Lables.append(dir)
            Path.append(f"{d}/{dir}/{imagePath}")

    if d == "Preprocessed/train":
        train["Lables"] = Lables
        train["Path"] = Path
        train.to_csv("train.csv")
    else:
        test["Lables"] = Lables
        test["Path"] = Path
        test.to_csv("test.csv")

print(train.head())
print(test.head())


