import numpy as np
from scipy import stats

def find_best_fit_distribution_continuous(data, distributions=None):
    """
    Find the best-fit distribution for the given data.

    Parameters:
        data (array-like): The data to fit the distributions to.
        distributions (list, optional): The candidate distributions to consider.
            Defaults to [stats.norm, stats.gamma, stats.expon, stats.uniform].

    Returns:
        best_distribution (scipy.stats.rv_continuous): The best-fit distribution.
        best_params (tuple): The parameters of the best-fit distribution.
    """
    if distributions is None:
        distributions = [
            stats.norm,      # Normal distribution
            stats.gamma,     # Gamma distribution
            stats.expon,     # Exponential distribution
            stats.uniform    # Uniform distribution
        ]

    best_distribution = None
    best_params = {}
    best_sse = np.inf

    for distribution in distributions:
        params = distribution.fit(data)
        sse = np.sum((distribution.pdf(data, *params) - data) ** 2)

        if sse < best_sse:
            best_distribution = distribution
            best_params = params
            best_sse = sse

    return best_distribution, best_params

def main()
    # Generate sample data
    np.random.seed(0)
    values = np.random.normal(loc=0, scale=1, size=1000)

    # Find the best-fit distribution
    best_distribution, best_params = find_best_fit_distribution_continuous(values)

    # Print the best-fit distribution and its parameters
    print(f"Best-fit distribution: {best_distribution.name}")
    print(f"Parameters: {best_params}")

if __name__ == '__main__':
    main()