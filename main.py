import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from model import portfolio_return, portfolio_variance, portfolio_standard_dev
from repository import get_data


def main():
    weights = np.array([0.5, 0.2, 0.2, 0.1])

    data = get_data()

    # # Calculate percentage returns
    returns = data.pct_change()
    returns["Portfolio"] = returns.dot(weights)
    # Calculate cumulative returns
    daily_cum_ret = (1 + returns).cumprod()
    # Plot the portfolio cumulative returns only
    fig, ax = plt.subplots()
    ax.plot(
        daily_cum_ret.index, daily_cum_ret.Portfolio, color="purple", label="portfolio"
    )
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
    plt.legend()
    plt.show()

    # Calculation
    port_return = portfolio_return(weights, data)
    port_variance = portfolio_variance(weights, data)
    port_standard_dev = portfolio_standard_dev(weights, data)

    # Display results
    print(f"port_return={port_return}")
    print(f"portfolio variance={str(np.round(port_variance, 4) * 100)}%")
    print(f"portfolio std={str(np.round(port_standard_dev, 4) * 100)}%")


if __name__ == "__main__":
    main()
