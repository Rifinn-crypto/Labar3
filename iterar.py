import pandas as pd
import os


 class DateIterator:


    def __init__(self):
        self.counter = 0
        self.df = pd.read_csv("C:/Users/esh20/Desktop/dataset.csv")


    def __next__(self) -> tuple:
        if os.path.exists("C:/Users/artyo/Desktop/dataset.csv"):
            if self.counter == self.df.shape[0]:
                raise StopIteration
            elif self.counter < self.df.shape[0]:
                    self.counter += 1
                    return self.df.loc[self.counter - 1]["Day"], self.df.loc[self.counter - 1]["Exchange rate"]
        raise FileNotFoundError



