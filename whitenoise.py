import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Simulation parameters
T = 100           # Length of the time series
mu = 0            # Mean of the noise
sigma = 1         # Standard deviation of the noise
np.random.seed(42) 

# White Noise Serie
X = np.random.normal(mu, sigma, T)

# Plot - Time Serie
plt.figure(figsize=(10, 4))
plt.plot(X, marker='o', linestyle='-', color='blue')
plt.title("White Noise Time Series")
plt.xlabel("Time step (t)")
plt.ylabel("Value of X_t")
plt.grid(True)
plt.show()

# Plot - Autocorrelation sample 
plot_acf(X, lags=20, alpha=0.05) 
plt.title("Sample Autocorrelation Function r(h)")
plt.xlabel("Lag (number of periods)")
plt.ylabel("Autocorrelation")
plt.show()
