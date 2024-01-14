from model import (
    portfolio_return,
    portfolio_variance,
    portfolio_standard_dev,
    portfolio_cumulative_returns,
)
from repository import get_data, get_weights
from view import display_chart, display_results


def main():
    weights = get_weights()
    data = get_data()

    # Calculation
    daily_cum_ret = portfolio_cumulative_returns(weights, data)
    port_return = portfolio_return(weights, data)
    port_variance = portfolio_variance(weights, data)
    port_standard_dev = portfolio_standard_dev(weights, data)

    # Display results
    display_chart(daily_cum_ret, "Portfolio")
    display_results(port_return, port_variance, port_standard_dev)


if __name__ == "__main__":
    main()
