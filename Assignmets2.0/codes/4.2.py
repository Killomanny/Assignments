import matplotlib.pyplot as plt
import numpy as np

T = np.loadtxt("tri.dat")
pts = 50
N = 10 ** 6

x = np.linspace(-6, 6, pts)

D = []

for i in range(0, pts):
    T.append(np.size(np.nonzero(T < x[i])) / N)

plt.plot(x.T, D, label="CDF")
plt.grid()
plt.xlabel("x")
plt.ylabel("$F_T(x)$")
plt.legend()
plt.show()
