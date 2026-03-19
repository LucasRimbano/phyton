#multiplicar matriz x matriz 

import numpy as np

matriz_A = np.arange(0,9).reshape(3,3)
matriz_B = np.array( [[2, 3, 4] ,
                     [3 , 4 , 2] ,
                     [3, 2 , 1 ]])

print("MATRIZ A:")
print(matriz_A)
print("Matriz B:")
print(matriz_B)


matriz_resultante = np.dot(matriz_A,matriz_B)
print(matriz_resultante)