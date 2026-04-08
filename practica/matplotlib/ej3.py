import matplotlib.pyplot as plt 
import numpy as np



def funcion():
    x = np.linspace(-10,10,10)
    y = 3 * x**2 + 1
    plt.plot (x,y)
    plt.xlabel("EJE X")
    plt.ylabel("EJE Y")
    plt.show()
    plt.grid()
funcion()    