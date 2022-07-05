import numpy as np
import matplotlib.pyplot as plt


N = 10**6
pts = 80
x = np.linspace(-4,4,pts)
SG = []


#Theory Graph
left = np.zeros(40)
main = np.linspace(0,1,10)
right = np.ones(30)
TG = np.concatenate([left,main, right])


#Analytical Graph
Uni = np.loadtxt("uni.dat",dtype='double')
for i in range(0,pts):
	SG.append(np.size(np.nonzero(Uni < x[i]))/N)

	
#Plotting Graphs	
plt.grid() #creating the grid	
plt.plot(x,SG,'bo') #plotting Stimulation CDF
plt.plot(x,TG,color="orange")   #plotting Theory CDF
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Simulation", "Analysis"])
plt.show()
