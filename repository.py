import numpy as np
import pandas as pd

# Proctor & Gamble, Microsoft, JP Morgan and General Electric
portfolio = {"GE": 0.5, "JPM": 0.2, "MSFT": 0.2, "PG": 0.1}


def get_weights() -> np.array:
    return np.array(portfolio.values())


def get_data():
    return pd.read_csv(
        r"input\small_portfolio.csv",
        delimiter=",",
        index_col="date",
        parse_dates=["date"],
    )


if __name__ == "__main__":
    print(get_weights())
