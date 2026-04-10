import matplotlib.pyplot as plt

datos = [5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 30]

datos.sort()
print("Datos ordenados:", datos)


def mediana(lista):
    n = len(lista)
    if n % 2 == 0:
        return (lista[n//2 - 1] + lista[n//2]) / 2
    else:
        return lista[n//2]


n = len(datos)

# Q2
q2 = mediana(datos)

# dividir en dos mitades
if n % 2 == 0:
    mitad_inferior = datos[:n//2]
    mitad_superior = datos[n//2:]
else:
    mitad_inferior = datos[:n//2]
    mitad_superior = datos[n//2 + 1:]

# Q1 y Q3
q1 = mediana(mitad_inferior)
q3 = mediana(mitad_superior)

# rango intercuartílico
ric = q3 - q1

# límites
limite_inferior = q1 - 1.5 * ric
limite_superior = q3 + 1.5 * ric

# atípicos
atipicos = []
for x in datos:
    if x < limite_inferior or x > limite_superior:
        atipicos.append(x)

print("\nRESULTADOS")
print("Q1 =", q1)
print("Q2 =", q2)
print("Q3 =", q3)
print("RIC =", ric)
print("Límite inferior =", limite_inferior)
print("Límite superior =", limite_superior)
print("Valores atípicos =", atipicos)

# boxplot
plt.boxplot(datos)
plt.title("Boxplot")
plt.show()