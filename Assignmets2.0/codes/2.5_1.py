import numpy as np
import matplotlib.pyplot as plt

X = np.loadtxt("../2.1/gau.dat")
N = 10**6
pts=100 

x = np.linspace(-10,10,pts)
def gauss_pdf(x):
        return (1/np.sqrt(2*np.pi))*np.exp(-(x**2/2))

F = []
for i in range(0,pts):
        F.append(np.size(np.nonzero(X < x[i]))/N) 

p = []
for i in range(0,pts-1):
        p.append( (F[i+1] - F[i])/ (x[i+1]-x[i]) )

vec_gauss=np.vectorize(gauss_pdf)

plt.plot(x,vec_gauss(x),label = "Theory",color = "orange")
plt.scatter(x[0:pts-1],p,label = "Numereical")
plt.grid()
plt.legend()
plt.show()
