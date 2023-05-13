import numpy as np
import matplotlib.pyplot as plt
from random import randint

def fractal_dimension_fourier(x):
    N = len(x)
    Xf = np.fft.fft(x)
    Sf = np.abs(Xf)**2
    k = np.arange(1, N//2)
    freqs = k / N
    p = np.polyfit(np.log(freqs), np.log(Sf[k]), 1)
    return 2 - p[0], p

def run_FR():
    # Generate a sample time series
    t = np.linspace(0, 1, 1000)
    x = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*10*t) + np.random.randn(len(t))*0.1

    with open ("time-series.txt", "w") as f:
        f.write("Time Series #" + str(randint(1, 10000)) + "\n\n\n============\n\n\nT-Value: " + str(t) + "\n\n\n============\n\n\n" + "X-Value: " + str(x))

    # Compute the fractal dimension using the Fourier analysis method
    fractal_dimension, p = fractal_dimension_fourier(x)

    # Plot the time series and the Fourier analysis results
    fig, axs = plt.subplots(1, 2, figsize=(10,5))
    axs[0].plot(t, x)
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Amplitude')
    axs[0].set_title('Sample Time Series')
    N = len(x)
    Xf = np.fft.fft(x)
    Sf = np.abs(Xf)**2
    k = np.arange(1, N//2)
    freqs = k / N
    axs[1].loglog(freqs, Sf[k], 'bo')
    axs[1].loglog(freqs, np.exp(p[1]) * freqs**(-p[0]), 'r')
    axs[1].set_xlabel('Frequency (log scale)')
    axs[1].set_ylabel('Power spectrum (log scale)')
    axs[1].set_title('Fractal Dimension Estimate')
    plt.savefig("graph.png")
    return (0, "fourier_analysis")
