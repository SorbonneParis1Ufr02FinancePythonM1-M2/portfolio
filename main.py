from model import portfolio_cumulative_returns, get_portfolio_indicators
from repository import get_data, get_weights, get_config
from view import display_chart, display_results


def main():
    config = get_config()
    weights = get_weights(config)
    data = get_data(config)

    # Calculation
    daily_cum_ret = portfolio_cumulative_returns(weights, data)
    indicators = get_portfolio_indicators(weights, data, config)

    # Display results
    display_chart(daily_cum_ret, config)
    display_results(indicators, config)


if __name__ == "__main__":
    main()
