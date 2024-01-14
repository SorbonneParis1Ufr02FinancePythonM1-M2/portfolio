import pandas as pd


def get_data():
    return pd.read_csv(
        r"input\small_portfolio.csv",
        delimiter=",",
        index_col="date",
        parse_dates=["date"],
    )


if __name__ == "__main__":
    print(dir())
