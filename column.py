import pandas as pd


def write_to_file(input_file: str, file_for_x: str, file_for_y: str) -> None:
    df = pd.read_csv(input_file)
