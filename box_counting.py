import numpy as np
import matplotlib.pyplot as plt
from random import randint

def fractal_dimension_boxcount(x, k):
    # Create a 2D grid of size k x k
    grid = np.zeros((k, k))

    # Map the data to the grid
    for i in range(len(x)):
        idx = int((x[i] - x.min()) / (x.max() - x.min()) * (k - 1))
        grid[idx, 0] += 1

    # Compute the box-counting dimension
    Ns = []
    for w in range(k//2, 1, -1):
        count = 0
        for i in range(w):
            for j in range(w):
                if grid[i,j] > 0:
                    count += 1
        Ns.append(count)

    if len(Ns) > 1:
        coeffs = np.polyfit(np.log(1/np.array(Ns[:-1])), np.log(np.array(Ns[1:])), 1)
        return -coeffs[0]
    else:
        return np.nan

def run_BC():
    # Generate a sample time series
    t = np.linspace(0, 1, 1000)
    x = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*10*t) + np.random.randn(len(t))*0.1

    # with open ("time-series.txt", "w") as f:
    #     f.write("Time Series #" + str(randint(1, 10000)) + "\n\n\n============\n\n\nT-Value: " + str(t) + "\n\n\n============\n\n\n" + "X-Value: " + str(x))


    # Compute the fractal dimension using the box-counting method
    fractal_dimension = fractal_dimension_boxcount(x, 20)

    # Plot the time series and the box-counting analysis results
    fig, axs = plt.subplots(1, 2, figsize=(10,5))
    axs[0].plot(t, x)
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Amplitude')
    axs[0].set_title('Sample Time Series')
    Ns = np.arange(1, len(x)//2, 2)
    counts = np.zeros(len(Ns))
    for i, N in enumerate(Ns):
        counts[i] = fractal_dimension_boxcount(x, N)
    axs[1].loglog(Ns, counts, 'bo')
    axs[1].set_xlabel('Box size (log scale)')
    axs[1].set_ylabel('Number of boxes (log scale)')
    axs[1].set_title('Fractal Dimension Estimate')
    plt.savefig("graph.png")
    return (0, "box_counting")
