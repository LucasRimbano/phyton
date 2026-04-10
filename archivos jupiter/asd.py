import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = x**2

plt.plot(x, y)
plt.grid()
plt.show()