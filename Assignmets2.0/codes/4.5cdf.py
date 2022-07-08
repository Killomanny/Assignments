import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

pts = 60
n = 10 ** 6



X = np.fromfile("tri.dat", dtype=float, count=n, sep='', offset=0)   #this is big X
x = np.linspace(-3, 3, pts)


# Empirical CDF
F = []
for i in range(0, pts):
    Fcount = np.count_nonzero(X < x[i])
    F.append(Fcount / n)
	
# Theoretical CDF
def gen_F_theory(xi):
    if (xi <= 0):
        return 0.0
    elif (xi <= 1):
        return xi * xi / 2
    elif (xi <= 2):
        return -xi * xi / 2 + 2 * xi - 1
    else:
        return 1.0


vecgen_F_theory = np.vectorize(gen_F_theory)
F_theory = vecgen_F_theory(x)



plt.scatter(x.T[0:(pts - 1)], P, color="blue", label="Empirical PDF")  # plotting the empirical CDF
plt.plot(x.T, F_theory, color="orange", label="Theoretical PDF")  # plotting the experimental CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$p_T(x)$")
plt.title("Theoretical PDF of T")
plt.legend(loc="best")
plt.show()
