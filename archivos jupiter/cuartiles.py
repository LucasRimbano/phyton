import numpy as np

numeros = [4, 6, 7, 8, 5, 9, 10, 7, 8, 9, 5, 6, 7, 8]

suma = sum(numeros)

promedio = suma / len(numeros)
print("Promedio:", promedio)


numeros = len(numeros)

if numeros % 2 == 0:
    mediana = (numeros[n//2 - 1] + numeros[n//2]) / 2
else:
    mediana = numeros[n//2]


if len(numeros) % 2 != 0:
    q1 = numeros[len(numeros) // 4]
    q3 = numeros[3 * len(numeros) // 4]
    print("Cuartil 1:", q1)
    print("Cuartil 3:", q3)
