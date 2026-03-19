import numpy as np 


transform1 = np.array([
    [0, -1],
    [1,  0]
])


transform2 = np.array([
    [1, 1],
    [0, 1]
])
vector  = np.array([1,2])

multiplicacion = transform2.dot(transform1)

vectorXmatriz = multiplicacion.dot(vector)

print("MULTIPLICACION COMBINADA:")
print(multiplicacion)

print("Resultado final")
print(vectorXmatriz)