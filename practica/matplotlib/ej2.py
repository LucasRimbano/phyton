import matplotlib.pyplot as plt  
import numpy as np

#producto escalar y graficar


def preguntarEscalar():
    numero = float(input("Ingrese un numero:"))
    return numero




n = preguntarEscalar()
print(f"El numero ingresado es:", n)


matriz  = np.arange(0,9).reshape(3,3)
print(matriz)

def productoEscalar(n,matriz):
    multiplicacion = np.dot(n,matriz)
    print("El resultado es:",multiplicacion)   

productoEscalar(n,matriz)



x = [1 ,2,3,4,5,6]
y = [50,10,0,5,20,100]

plt.plot(x,y)
plt.title("Ventas x dia")
plt.xlabel("Dias")
plt.ylabel("Cantidad vendida")
plt.grid()
plt.bar(x,y)
plt.show() 