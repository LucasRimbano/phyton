import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)


f = 3*x**2 + 1


x0 = 3
y0 = 3*x0**2 + 1
m = 18


tangent = m*(x - x0) + y0

plt.figure()
plt.plot(x, f, label="f(x) = 3x^2 + 1")
plt.plot(x, tangent, linestyle='--', label="Tangente en x=3")
plt.scatter([x0], [y0])

plt.xlabel("x")
plt.ylabel("y")
plt.title("Función y recta tangente")
plt.legend()
plt.grid()

plt.show()