import numpy as np

from model import (
    portfolio_return,
    portfolio_variance,
    portfolio_standard_dev,
    portfolio_cumulative_returns,
)
from repository import get_data
from view import display_chart


def main():
    weights = np.array([0.5, 0.2, 0.2, 0.1])
    data = get_data()

    # Calculation
    daily_cum_ret = portfolio_cumulative_returns(weights, data)
    port_return = portfolio_return(weights, data)
    port_variance = portfolio_variance(weights, data)
    port_standard_dev = portfolio_standard_dev(weights, data)

    # Display results
    display_chart(daily_cum_ret, "Portfolio")


    print(f"port_return={port_return}")
    print(f"portfolio variance={str(np.round(port_variance, 4) * 100)}%")
    print(f"portfolio std={str(np.round(port_standard_dev, 4) * 100)}%")


if __name__ == "__main__":
    main()
