import numpy as np

print("Ingresá los valores de la matriz A (2x2):")
A = []
for i in range(2):
    fila = []
    for j in range(2):
        valor = float(input(f"A[{i}][{j}]: "))
        fila.append(valor)
    A.append(fila)

print("\nIngresá los valores de la matriz B (2x2):")
B = []
for i in range(2):
    fila = []
    for j in range(2):
        valor = float(input(f"B[{i}][{j}]: "))
        fila.append(valor)
    B.append(fila)


A = np.array(A)
B = np.array(B)


resultado = A @ B
resultado2 = np.dot(A, B)

print("\nMatriz A:")
print(A)

print("\nMatriz B:")
print(B)

print("\nResultado con @:")
print(resultado)

print("\nResultado con np.dot:")
print(resultado2)