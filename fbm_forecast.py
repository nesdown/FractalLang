import numpy as np
import matplotlib.pyplot as plt

def fractional_brownian_motion(H, N):
    """Generate a sample of fractional Brownian motion."""
    R = np.random.randn(N)
    X = np.zeros(N)
    X[0] = R[0]
    for i in range(1, N):
        X[i] = H*X[i-1] + (1-H)*R[i]
    return X

def forecast_fbhm(x, H, N):
    """Forecast a time series using fractional Brownian motion."""
    N0 = len(x)
    X = np.zeros(N)
    X[:N0] = x
    for i in range(N0, N):
        X[i] = H*X[i-1] + (1-H)*np.random.randn()
    return X

def run_FMB():
    # Generate a sample of fractional Brownian motion
    N = 1000
    H = 0.6
    x = fractional_brownian_motion(H, N)

    # Forecast the time series using fractional Brownian motion
    N_forecast = 500
    x_forecast = forecast_fbhm(x, H, len(x) + N_forecast)

    # Plot the sample and forecast time series
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    axs[0].plot(np.arange(N), x)
    axs[0].plot(np.arange(N, N+len(x_forecast[:len(x)])), x_forecast[:len(x)])
    # axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Amplitude')
    axs[0].set_title('Sample Time Series vs Forecast Time Series')
    axs[1].plot(np.arange(N+len(x), N+len(x_forecast)), x_forecast[len(x):])
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Amplitude')
    # axs[1].set_title('Forecast Time Series')
    
    fig.set_size_inches(10, 5)
    plt.savefig("graph.png")
    return (0, "fBm_forecasting")

