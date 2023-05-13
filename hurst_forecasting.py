import numpy as np
import matplotlib.pyplot as plt

def hurst_exponent(x):
    """Estimate the Hurst exponent of a time series."""
    if np.std(x) == 0:
        return 0.5
    x = (x - np.mean(x)) / np.std(x)
    N = len(x)
    T = np.arange(1, N+1)
    Y = np.cumsum(x - np.mean(x))
    R = np.zeros(N)
    for i in range(N):
        S = np.std(Y[:i+1])
        if S == 0:
            R[i] = 1e-10
        else:
            R[i] = np.max(Y[:i+1]) - np.min(Y[:i+1])
            R[i] /= S
    R = np.log(R)
    T = np.log(T)
    # Remove NaN and infinite values
    R = R[np.isfinite(R) & np.isfinite(T)]
    T = T[np.isfinite(R) & np.isfinite(T)]
    p = np.polyfit(T, R, 1)
    return p[0] / 2

def fractional_brownian_motion(H, N):
    """Generate a sample of fractional Brownian motion."""
    R = np.random.randn(N)
    X = np.zeros(N)
    X[0] = R[0]
    for i in range(1, N):
        X[i] = H*X[i-1] + (1-H)*R[i]
    return X

def run_H():
    # Generate a sample of fractional Brownian motion
    N = 1000
    H = 0.6
    x = fractional_brownian_motion(H, N)

    # Compute the Hurst exponent and fractal dimension
    hurst = hurst_exponent(x)
    fractal_dimension = 2 - hurst

    # Plot the sample and the analysis results
    fig, axs = plt.subplots(1, 2, figsize=(10,5))
    axs[0].plot(x)
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Amplitude')
    axs[0].set_title('Sample Time Series')
    Ns = np.arange(1, len(x)//2, 2)
    counts = np.zeros(len(Ns))
    for i, N in enumerate(Ns):
        counts[i] = hurst_exponent(x[:N])
    axs[1].loglog(Ns, counts, 'bo')
    axs[1].set_xlabel('Window size (log scale)')
    axs[1].set_ylabel('Hurst exponent (log scale)')
    axs[1].set_title('Fractal Dimension Estimate')
    
    plt.savefig("graph.png")
    return (0, "hurst_forecasting")
