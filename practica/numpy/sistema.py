import numpy as np


def cargar_matriz(n):
    matriz = []
    print(f"\nIngresá la matriz A ({n}x{n}):")
    
    for i in range(n):
        fila = []
        for j in range(n):
            valor = float(input(f"A[{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    
    return np.array(matriz, dtype=float)



def cargar_vector(n):
    vector = []
    print(f"\nIngresá el vector B ({n}x1):")
    
    for i in range(n):
        valor = float(input(f"B[{i}]: "))
        vector.append([valor])
    
    return np.array(vector, dtype=float)




n = int(input("Ingresá el tamaño de la matriz (n para matriz nxn): "))

A = cargar_matriz(n)
B = cargar_vector(n)

print("\nMatriz A:")
print(A)

print("\nVector B:")
print(B)



detA = np.linalg.det(A)
print("\nDeterminante de A:")
print(detA)

if detA == 0:
    print("La matriz no tiene inversa (determinante = 0)")
    exit()



cofactores = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        menor = np.delete(np.delete(A, i, axis=0), j, axis=1)
        cofactores[i, j] = ((-1) ** (i + j)) * np.linalg.det(menor)

print("\nMatriz de cofactores:")
print(cofactores)



adjunta = cofactores.T
print("\nAdjunta de A:")
print(adjunta)



A_inv = adjunta / detA
print("\nInversa de A:")
print(A_inv)



X = A_inv @ B
print("\nSolución del sistema:")

for i in range(n):
    print(f"x{i+1} =", X[i, 0])