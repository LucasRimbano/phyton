import matplotlib.pyplot as plt 
import numpy as np

def funcion():
    x = np.linspace(-20,20,100)
    y = x**2 + 2*x

    plt.plot(x,y)
    plt.xlabel("eje x")
    plt.ylabel("eje y")
    plt.title("f(X)= x**2 + x*2")
    plt.show()

funcion()    