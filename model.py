from typing import Dict

import numpy as np
import pandas as pd


def portfolio_return(weights: np.array, data_portfolio: pd.DataFrame) -> np.float64:
    """
    Calculate expected portfolio performance
    The sum of the weights must be 1
    :param weights: weights as a vector -> np.array([0.5, 0.2, 0.2, 0.1])
    :param data_portfolio: stock prices
    :return: the portfolio return
    """
    np.testing.assert_almost_equal(np.sum(weights), 1)
    returns = data_portfolio.pct_change()
    mean_daily_returns = returns.mean()
    return np.sum(mean_daily_returns * weights)


def portfolio_variance(weights: np.array, data_portfolio: pd.DataFrame) -> np.float64:
    """
    Calculate expected portfolio variance
    The sum of the weights must be 1
    :param weights: weights as a vector -> np.array([0.5, 0.2, 0.2, 0.1])
    :param data_portfolio: stock prices
    :return: the portfolio variance
    """
    np.testing.assert_almost_equal(np.sum(weights), 1)
    returns = data_portfolio.pct_change()
    cov_matrix = (returns.cov()) * 250
    return np.dot(weights.T, np.dot(cov_matrix, weights))


def portfolio_standard_dev(weights: np.array, data_portfolio: pd.DataFrame) -> np.float64:
    """
        Calculate expected portfolio standard deviation
        The sum of the weights must be 1
        :param weights: weights as a vector -> np.array([0.5, 0.2, 0.2, 0.1])
        :param data_portfolio: stock prices
        :return: the portfolio standard deviation
        """
    np.testing.assert_almost_equal(np.sum(weights), 1)
    return np.sqrt(portfolio_variance(weights, data_portfolio))


def portfolio_cumulative_returns(weights: np.array, data_portfolio: pd.DataFrame, config: Dict):
    new_column = config["initialisation"]["portfolio_column"]
    returns = asset_and_portfolio_cumulative_returns(weights, data_portfolio, config)
    result = returns[[new_column]]
    return result


def asset_and_portfolio_cumulative_returns(weights: np.array, data_portfolio: pd.DataFrame, config: Dict):
    new_column = config["initialisation"]["portfolio_column"]
    returns = data_portfolio.pct_change()
    returns[new_column] = returns.dot(weights)
    return (1 + returns).cumprod()


def get_portfolio_indicators(weights: np.array, data_portfolio: pd.DataFrame, config: Dict) -> Dict:
    results = {}
    port_return = portfolio_return(weights, data_portfolio)
    port_variance = portfolio_variance(weights, data_portfolio)
    port_standard_dev = portfolio_standard_dev(weights, data_portfolio)

    results[config['view']['return']] = port_return
    results[config['view']['variance']] = port_variance
    results[config['view']['std']] = port_standard_dev

    return results
