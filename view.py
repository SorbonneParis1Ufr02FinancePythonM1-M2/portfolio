import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def display_chart(data: pd.DataFrame, column: str, color="purple") -> None:
    fig, ax = plt.subplots()
    ax.plot(data.index, data[column], color=color, label=column)
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
    plt.legend()
    plt.show()


def display_results(
    portfolio_return: np.float64,
    portfolio_variance: np.float64,
    portfolio_standard_dev: np.float64,
) -> None:
    print(f"port_return={portfolio_return}")
    print(f"portfolio variance={str(np.round(portfolio_variance, 4) * 100)}%")
    print(f"portfolio std={str(np.round(portfolio_standard_dev, 4) * 100)}%")
