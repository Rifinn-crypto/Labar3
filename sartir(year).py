import pandas as pd
from typing import NoReturn


def formatted_file(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file)

    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day1"] = df["Day"].dt.date
    df["Year"] = df["Day"].dt.year
    return df


def write_to_file(input_file: str, year: int) -> NoReturn:
    df = formatted_file(input_file)

    df = df[df["Year"] == year]
    data = str(df["Day1"].iloc[0]).replace("-", "") + "_" + str(df["Day1"].iloc[df.shape[0] - 1]).replace("-", "")
    del df["Year"]
    del df["Day1"]
    df.to_csv(data + ".csv", index=False)