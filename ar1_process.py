import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
import statsmodels.api as sm

# Parameters
phi = 0.7       # Autoregresive coefficient
sigma = 1.0     # SD of noise
T = 200         # of Observations

np.random.seed(42)

# Epislon with Normalization condition
epsilon = np.random.normal(0, sigma, T)

# Initialize process
X = np.zeros(T)

# Simulation of AR(1): X_t = phi * X_{t-1} + epsilon_t
for t in range(1, T):
    X[t] = phi * X[t - 1] + epsilon[t]

# (a) Plot of time series and autorcorrelation
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(X, color='royalblue')
plt.title("Simulated AR(1) Process (phi = 0.7)")
plt.xlabel("Time")
plt.ylabel("X_t")

plt.subplot(1, 2, 2)
plot_acf(X, lags=20, ax=plt.gca())
plt.title("Autocorrelation Function (ACF)")

plt.tight_layout()
plt.show()

# (b) Estimate phi with linear regression model
# Xt = beta * X_{t-1} + epsilon_t
X_lag = X[:-1]        # X_{t-1}
X_current = X[1:]      # X_t

X_lag_const = sm.add_constant(X_lag)
model = sm.OLS(X_current, X_lag_const).fit() # Model = Minimum ordinary squares
estimated_phi = model.params[1] 

# (c) Value comparison between phi value and true value (0.7)
print("True phi value:      ", phi)
print("Estimated phi value: ", round(estimated_phi, 4))
print(model.summary())

# (d) Discussion when |phi| >= 1
"""
Si |phi| >= 1, el proceso no es estacionario:
- Para phi = 1, se convierte en una serie de tiempo en la que cada valor depende del anterior (la varianza crece indefinidamente con el tiempo).
- Para |phi| > 1, los valores crecen en magnitud (lo que provoca que se alejen de manera indefinida de la media +infinito o -infinito).

En ambos casos, la media y la varianza dejan de ser constantes a lo largo del tiempo.
"""
