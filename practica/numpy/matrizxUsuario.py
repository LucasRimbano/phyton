import numpy as np

def cargar_matriz(nombre, filas, columnas):
    print(f"\nCargando matriz {nombre}:")
    matriz = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"{nombre}[{i}][{j}] = "))
            fila.append(valor)
        matriz.append(fila)

    return np.array(matriz)



filas_A = int(input("Filas de A: "))
columnas_A = int(input("Columnas de A: "))

filas_B = int(input("Filas de B: "))
columnas_B = int(input("Columnas de B: "))


if columnas_A != filas_B:
    print("\n❌ No se pueden multiplicar las matrices")
    print("Las columnas de A deben ser iguales a las filas de B")
else:
    
    A = cargar_matriz("A", filas_A, columnas_A)
    B = cargar_matriz("B", filas_B, columnas_B)

   
    resultado = A @ B

    print("\nMatriz A:")
    print(A)

    print("\nMatriz B:")
    print(B)

    print("\nResultado A x B:")
    print(resultado)