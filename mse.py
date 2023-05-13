import numpy as np
import matplotlib.pyplot as plt

def approximate_entropy(x, m, r):
    """
    Calculate the approximate entropy of a time series.
    
    Parameters:
        x (array-like): The input time series.
        m (int): The length of the compared subseries. Typical values range from 1 to 5.
        r (float): Tolerance for considering two values to be similar. Typical values range from 0.1 to 0.3 times
                   the standard deviation of the input time series.
    
    Returns:
        ae (float): The approximate entropy of the input time series.
    """
    n = len(x)
    Cm = []
    for i in range(n - m + 1):
        subseries = x[i:i+m]
        count = 0
        for j in range(n - m + 1):
            if i != j:
                subseries2 = x[j:j+m]
                if max(abs(subseries - subseries2)) <= r:
                    count += 1
        Cm.append(count)
    Cm = np.array(Cm)
    Cm_mean = np.mean(Cm) + 1e-10
    Cm_plus1_mean = np.mean(np.roll(Cm, -1)) + 1e-10
    ae = np.log(Cm_mean / Cm_plus1_mean)
    return ae

def run_MSE():
    # Generate a sample time series
    t = np.linspace(0, 1, 1000)
    x = np.sin(2 * np.pi * 10 * t) + np.random.normal(0, 0.1, 1000)

    # Set the number of points for forecasting
    N_forecast = 100

    # Calculate approximate entropy of the time series
    m = 2
    r = 0.2 * np.std(x)
    ae = approximate_entropy(x, m, r)

    # Generate the forecasted time series
    x_forecast = np.zeros(len(x) + N_forecast)
    x_forecast[:len(x)] = x
    for i in range(len(x), len(x) + N_forecast):
        # Generate a surrogate time series using the residuals of the original time series
        x_surrogate = np.random.normal(0, np.std(x), len(x))
        for j in range(1, len(x)):
            x_surrogate[j] = x_surrogate[j-1] + x[j-1] - np.mean(x)
        x_forecast[i] = x_surrogate[-1] + np.random.normal(0, np.sqrt(np.var(x)), 1)

    # Calculate approximate entropy of the forecasted time series
    ae_forecast = approximate_entropy(x_forecast, m, r)

    # Plot the time series and the forecasted time series
    # plt.figure(figsize=(10, 4))
    # plt.plot(t, x, label='Original Time Series')
    # plt.plot(t[-1] + np.linspace(0, 1, N_forecast + 1)[1:], x_forecast[-N_forecast:], label='Forecasted Time Series')
    # plt.legend()
    # plt.xlabel('Time')
    # plt.ylabel('Amplitude')
    # plt.title('Approximate Entropy Time Series Forecasting')

    # Plot the difference between the original and forecasted time series
    # ae_diff = np.abs(x[-N_forecast:] - x_forecast[-N_forecast:])
    # ae_mean = np.mean(ae_diff) + 1e-10
    # ae_std = np.std(ae_diff) + 1e-10
    # ae_z = (ae_diff - ae_mean) / ae_std

    # plt.figure(figsize=(10, 4))
    # plt.plot(t[-N_forecast:], ae_z)
    # plt.xlabel('Time')
    # plt.ylabel('Amplitude')
    # plt.title('Z-Scores of the Difference between Original and Forecasted Time Series')


    plt.figure(figsize=(3.65, 1.37), dpi=300)
    plt.plot(t, x, label='Original Time Series', linewidth=0.5)
    plt.plot(t[-1] + np.linspace(0, 1, N_forecast + 1)[1:], x_forecast[-N_forecast:], label='Forecasted Time Series', linewidth=0.5)
    plt.legend(fontsize=3)
    plt.xlabel('Time', fontsize=4)
    plt.ylabel('Amplitude', fontsize=4)
    plt.title('Approximate Entropy Time Series Forecasting', fontsize=5)

    plt.tick_params(axis='x', labelsize=3)
    plt.tick_params(axis='y', labelsize=3)

    plt.savefig('graph.png', bbox_inches='tight')

    # fig.set_size_inches(10, 5)
    # plt.savefig("graph.png")
    return (0, "MSE_forecasting")
