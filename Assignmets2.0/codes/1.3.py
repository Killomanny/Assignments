import numpy as np
import matplotlib.pyplot as plt


pts = 50
x = np.linspace(-4,4,pts)
F = []


def uniform_cdf(x):
        if(x<0):
                return 0
        elif(x>1):
                return 1
        else:
                return x


vec_uniform = np.vectorize(uniform_cdf)


plt.plot(x.T, vec_uniform(x), color="orange" )#plotting the CDF
plt.grid()
plt.legend()
plt.xlabel("x")
plt.ylabel("$F_U(x)$")
plt.show()
