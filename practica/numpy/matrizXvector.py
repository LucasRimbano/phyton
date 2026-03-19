#producto de matriz x vector 
import numpy as np

matriz = np.arange(1,10).reshape(3,3)

print(matriz)



vector = np.array([2,2,2])

matriz_Nueva = matriz.dot(vector)
print(matriz_Nueva)

