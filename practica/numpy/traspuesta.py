import numpy as np

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

matriz = []

print("Ingrese los valores de la matriz:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

matriz = np.array(matriz)

print("\nMatriz original:")
print(matriz)

traspuesta = matriz.T

print("\nMatriz traspuesta:")
print(traspuesta)