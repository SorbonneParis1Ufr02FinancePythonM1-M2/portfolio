from model import (
    portfolio_return,
    portfolio_variance,
    portfolio_standard_dev,
    portfolio_cumulative_returns,
)
from repository import get_data, get_weights, get_config
from view import display_chart, display_results


def main():
    config = get_config()
    weights = get_weights(config)
    data = get_data(config)

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
