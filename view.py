from typing import Dict

import matplotlib
import pandas as pd
from matplotlib import pyplot as plt


def display_chart(data: pd.DataFrame, config: Dict) -> None:
    print(config)
    fig, ax = plt.subplots()
    ax.plot(
        data.index,
        data[config["chart"]["column"]],
        color=config["chart"]["color"],
        label=config["chart"]["label"],
    )
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
    plt.legend()
    plt.show()


def display_results(results: Dict, config: Dict) -> None:
    df = pd.DataFrame.from_dict(
        results, orient="index", columns=[config["view"]["column_values"]]
    )
    print(df)
