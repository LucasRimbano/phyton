import numpy as np
import matplotlib.pyplot as plt

def funcion():
    x = np.linspace(0, 10, 100)
    y = x**2 + 2

    plt.plot(x, y)
    plt.title("f(x) = x^2 + 2")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.grid()

    plt.show()

funcion()