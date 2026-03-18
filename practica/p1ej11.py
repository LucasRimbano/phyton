#generar una matriz 'mat' de 4x4 con datos random
#obtener la suma de los valores de mat
#objtener la desviacion estandar d elos valores de mat
#obtener las sumas de las columnas de mat 

import numpy as np

mat = np.random.randint(0,100,(4,4))
print(mat)


def sumatoriaTotal():
    print("La suma total es de:",np.sum(mat))

sumatoriaTotal()

def desviacionEstandar():
    print("La desviacion estandar es de:",np.std(mat))

desviacionEstandar()

def sumaColumnas(matriz):
    return np.sum(matriz, axis=0)

print(f"La suma de las columnas es: {sumaColumnas(mat)}")