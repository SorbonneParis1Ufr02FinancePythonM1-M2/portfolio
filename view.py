import matplotlib
import pandas as pd
from matplotlib import pyplot as plt


def display_chart(data: pd.DataFrame, column: str, color="purple"):
    fig, ax = plt.subplots()
    ax.plot(
        data.index, data[column], color=color, label=column
    )
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
    plt.legend()
    plt.show()