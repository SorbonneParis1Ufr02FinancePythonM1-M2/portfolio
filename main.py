import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def main():
    # https://campus.datacamp.com/courses/introduction-to-portfolio-analysis-in-python/introduction-to-portfolio-analysis?ex=6
    data = pd.read_csv(r'input\small_portfolio.csv', delimiter=',', index_col='date', parse_dates=['date'])

    # Calculate percentage returns
    returns = data.pct_change()

    # Calculate individual mean returns
    meanDailyReturns = returns.mean()

    # Define weights for the portfolio
    weights = np.array([0.5, 0.2, 0.2, 0.1])

    # Calculate expected portfolio performance
    portReturn = np.sum(meanDailyReturns * weights)

    # Print the portfolio return
    print(portReturn)

    # https: // campus.datacamp.com / courses / introduction - to - portfolio - analysis - in -python / introduction - to - portfolio - analysis?ex = 7
    # Create portfolio returns column
    returns['Portfolio'] = returns.dot(weights)

    # Calculate cumulative returns
    daily_cum_ret = (1 + returns).cumprod()

    # Plot the portfolio cumulative returns only
    fig, ax = plt.subplots()
    ax.plot(daily_cum_ret.index, daily_cum_ret.Portfolio, color='purple', label="portfolio")
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
    plt.legend()
    plt.show()

    # https: // campus.datacamp.com / courses / introduction - to - portfolio - analysis - in -python / introduction - to - portfolio - analysis?ex = 9
    # Get percentage daily returns
    daily_returns = data.pct_change()

    # Assign portfolio weights
    weights = np.array([0.05, 0.4, 0.3, 0.25])

    # Calculate the covariance matrix
    cov_matrix = (daily_returns.cov()) * 250

    # Calculate the portfolio variance
    port_variance = np.dot(weights.T, np.dot(cov_matrix, weights))

    # Print the result
    print(str(np.round(port_variance, 4) * 100) + '%')

    # https: // campus.datacamp.com / courses / introduction - to - portfolio - analysis - in -python / introduction - to - portfolio - analysis?ex = 10
    # Calculate the standard deviation by taking the square root
    port_standard_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    # Print the results
    print(str(np.round(port_standard_dev, 4) * 100) + '%')


if __name__ == '__main__':
    main()