import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp

pts=50
x=np.linspace(-6,6,pts)
X=np.loadtxt("../2.1/gau.dat")
N=10**6

def Q(x):
    return (1 - mp.erf(x/np.sqrt(2)))/2
 
def gauss(x):
        return 1 - Q(x)

vec_gauss=np.vectorize(gauss)

F_sim=[]
for i in range(0,pts):
        F_sim.append(np.size(np.nonzero(X < x[i]))/N)

plt.plot(x.T,vec_gauss(x),label="Theoretical",color="orange")
plt.scatter(x.T,F_sim,label="Numerical")
plt.grid()
plt.xlabel("x")
plt.ylabel("$F_X(x)$")
plt.legend()
plt.show()
