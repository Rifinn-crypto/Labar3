import pandas as pd


def write_to_file(input_file: str, file_for_x: str, file_for_y: str) -> None:
    df = pd.read_csv(input_file)
    df["Day"].to_csv(file_for_x, index=False)
    df["Exchange rate"].to_csv(file_for_y, index=False)