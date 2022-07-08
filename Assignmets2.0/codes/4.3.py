import matplotlib.pyplot as plt
import numpy as np

T=np.loadtxt("../4.1/tri.dat")
pts=100
N=10**6

x=np.linspace(-6,6,pts)

F=[]
for i in range(0,pts):
        F.append(np.size(np.nonzero(T < x[i]))/N)

p=[]
for i in range(0,pts-1):
	p.append((F[i+1]-F[i])/(x[i+1]-x[i]))

plt.plot(x[0:pts-1],p,label="PDF")
plt.grid()
plt.xlabel("x")
plt.ylabel("$p_T(x)$")
plt.legend()
plt.show()
