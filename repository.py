import numpy as np
import pandas as pd


def get_weights() -> np.array:
    return np.array([0.5, 0.2, 0.2, 0.1])


def get_data():
    return pd.read_csv(
        r"input\small_portfolio.csv",
        delimiter=",",
        index_col="date",
        parse_dates=["date"],
    )


if __name__ == "__main__":
    print(dir())
