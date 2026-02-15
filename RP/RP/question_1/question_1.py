import numpy as np
import matplotlib.pyplot as plt
from math import factorial, exp

# (a) Poisson1: inter-arrival times
def Poisson1(lam):
    t = 0
    arrivals = []
    while True:
        t += np.random.exponential(1/lam)
        if t > 1:
            break
        arrivals.append(t)
    return arrivals

# (b) Poisson2: number first, then arrival times
def Poisson2(lam):
    N = np.random.poisson(lam)
    arrivals = np.sort(np.random.uniform(0, 1, N))
    return arrivals

# (c) simulation
lam = 10
rounds = 10000

counts1 = np.array([len(Poisson1(lam)) for _ in range(rounds)])
counts2 = np.array([len(Poisson2(lam)) for _ in range(rounds)])

# empirical distributions
max_k = max(counts1.max(), counts2.max())
k_vals = np.arange(0, max_k + 1)

emp1 = np.array([np.mean(counts1 == k) for k in k_vals])
emp2 = np.array([np.mean(counts2 == k) for k in k_vals])

# theoretical Poisson(λ)
theory = np.array([(lam**k * exp(-lam)) / factorial(k) for k in k_vals])

# plot
plt.figure()
plt.plot(k_vals, emp1, marker='o', linestyle='')
plt.plot(k_vals, emp2, marker='x', linestyle='')
plt.plot(k_vals, theory, linestyle='-')
plt.xlabel("Number of arrivals on [0,1]")
plt.ylabel("Probability")
plt.show()
