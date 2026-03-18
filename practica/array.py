## Ejercicio 11
# Generar una matriz "mat" de 4x4 con datos random
#Obtener la suma de los valores de mat
# Obtener la desviación estándar de los valores de mat
# Obtener las sumas de las columnas de mat


import numpy as np

mat = np.random.randint(0,100,(4,4))
print(mat)

def Sumatotal():
    print("La suma total es:" , np.sum(mat))

Sumatotal()

numero = 5 

def productoEscalar():

    resultado = np.dot(mat, numero)
    print("El producto escalar es:",resultado )

def desviacionEstandar():
     print("La desviacion estandar es:",np.std(mat))
    
desviacionEstandar()

def sumaColumnas():
    print("La suma de las columnas es:" , np.sum(mat,axis = 0))

sumaColumnas()   


def sumaFilas():
    print("La suma de las filas:" ,np.sum(mat,axis = 1))

sumaFilas()