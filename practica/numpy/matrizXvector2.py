#como quiere el profe la dierencia es transformacion lineal
#
import numpy as np

matriz_i = np.array([2,0])
matriz_j = np.array([0,3])

base = np.array([matriz_i ,matriz_j]).transpose()


vector = np.array([1,1])

matriz_resultante = base.dot(vector)

print(matriz_resultante)


