from typing import Dict

import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from pandasgui import show


def _display_chart(data: pd.DataFrame, config: Dict) -> None:
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


def display_results(
    results: Dict, all_returns: pd.DataFrame, ptf_returns: pd.DataFrame, config: Dict
) -> None:
    indicators = pd.DataFrame.from_dict(
        results, orient="index", columns=[config["view"]["column_values"]]
    )

    if config["view_mode"]["print"]:
        _results_to_console(indicators, all_returns)

    if config["view_mode"]["pandasgui"]:
        _results_to_pandasgui(indicators, all_returns)

    if config["view_mode"]["chart"]:
        _display_chart(ptf_returns, config)


def _results_to_console(indicators: pd.DataFrame, all_returns: pd.DataFrame):
    print(indicators)
    print("*" * 20)
    print(f"returns shape={all_returns.shape}")


def _results_to_pandasgui(indicators: pd.DataFrame, all_returns: pd.DataFrame):
    show(indicators, all_returns)
