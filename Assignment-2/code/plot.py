import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 15, 20)
y = 5 * (x + 1) / 4

plt.plot(x, y, '-r', label='4y=5x+5')
plt.xlabel('x', color='k')
plt.ylabel('y', color='k')
plt.legend(loc='upper left')
plt.grid()

plt.show()
