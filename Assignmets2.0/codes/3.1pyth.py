import matplotlib.pyplot as plt
import numpy as np

C = np.loadtxt("custom.dat", dtype='double')

N = 10 ** 6
pts = 40

x = np.linspace(-5, 5, pts)

F_sim = []
for i in range(0, pts):
    F_sim.append(np.size(np.nonzero(C < x[i])) / N)


def exp_cdf(x):
    if x <= 0:
        return 0.0
    else:
        return (1 - np.exp(-x / 2))


vec_exp = np.vectorize(exp_cdf, otypes=['double'])

plt.plot(x, F_sim, 'o', label="Empirical", color="blue")
plt.plot(x, vec_exp(x), label="Theoritical", color="orange")
plt.grid()
plt.xlabel("x")
plt.ylabel("$F_V(x)$")
plt.legend()
plt.show()
