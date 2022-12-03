import pandas as pd
from typing import NoReturn


def formatted_file(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file)

    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day1"] = df["Day"].dt.date
    df["Year"] = df["Day"].dt.year
    return df
