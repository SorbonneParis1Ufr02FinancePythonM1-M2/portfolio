from model import (
    portfolio_cumulative_returns,
    get_portfolio_indicators,
    asset_and_portfolio_cumulative_returns,
)
from repository import get_data, get_weights, get_config
from view import display_results


def main():
    config = get_config()
    weights = get_weights(config)
    data = get_data(config)

    # Calculation
    daily_cum_ret = portfolio_cumulative_returns(weights, data, config)
    indicators = get_portfolio_indicators(weights, data, config)
    cumulative_returns = asset_and_portfolio_cumulative_returns(weights, data, config)

    # Display results
    display_results(indicators, cumulative_returns, daily_cum_ret, config)


if __name__ == "__main__":
    main()
