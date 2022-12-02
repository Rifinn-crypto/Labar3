import pandas as pd
import os


 class DateIterator:


    def __init__(self):
        self.counter = 0
        self.df = pd.read_csv("C:/Users/esh20/Desktop/dataset.csv")


    def __next__(self) -> tuple:
        if os.path.exists("C:/Users/esh20/Desktop/dataset.csv"):
            if self.counter == self.df.shape[0]:
                raise StopIteration
            elif self.counter < self.df.shape[0]:
                    self.counter += 1
                    return self.df.loc[self.counter - 1]["Day"], self.df.loc[self.counter - 1]["Exchange rate"]
        raise FileNotFoundError

 class DateIteratorXY:

    def __init__(self):

        self.counter = 0
        self.xf = pd.read_csv("C:/Users/esh20/PycharmProjects/Lab2/1/X.csv")
        self.yf = pd.read_csv("C:/Users/esh20/PycharmProjects/Lab2/1/Y.csv")

    def __next__(self) -> tuple:
        if self.counter == self.xf.shape[0]:
            raise StopIteration

        elif self.counter < self.xf.shape[0]:
            self.counter += 1
            return self.xf.loc[self.counter - 1]["Day"], self.yf.loc[self.counter - 1]["Exchange rate"]


