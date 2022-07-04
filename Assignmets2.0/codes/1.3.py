import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pts = 50
n = 10**6
U = pd.read_csv("../1.1/uni.dat")

x = np.linspace(-2,2,pts)
F = []

def uniform_cdf(x):
        if(x<0):
                return 0
        elif(x>1):
                return 1
        else:
                return x

F_theory=[]

vec_uniform = np.vectorize(uniform_cdf)

for i in range(0,pts):
        F_n = np.count_nonzero(U < x[i]) #checking probability condition
        F.append(F_n/n) #storing the probability values in a list

plt.scatter(x.T, F, color="blue" )#plotting the CDF
plt.plot(x.T, vec_uniform(x), color="orange" )#plotting the CDF
plt.grid()
plt.legend()
plt.xlabel("x")
plt.ylabel("$F_U(x)$")
plt.show()
