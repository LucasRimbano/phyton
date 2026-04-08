import numpy as np


A = np.array([
    [4, 2, 4],
    [5, 3, 7],
    [9, 3, 6]
], dtype=float)


B = np.array([
    [44],
    [56],
    [72]
], dtype=float)


detA = np.linalg.det(A)
print("Determinante de A:")
print(detA)




cofactores = np.zeros((3, 3))

for i in range(3):
    for j in range(3):
       
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
print("\nSolución:")
print(X)

print("\nx =", X[0, 0])
print("y =", X[1, 0])
print("z =", X[2, 0])