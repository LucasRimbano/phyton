import matplotlib.pyplot as plt
import numpy as np


numeros = [4,7,9,10,6,12,8,11,30,5,13]

numeros.sort()
print("Datos ordenados:", numeros)



def calcular_mediana(datos):
    n = len(datos)

    if n % 2 == 0:
        return (datos[n//2 - 1] + datos[n//2]) / 2
    else:
        return datos[n//2]


def calcular_cuartil(datos, k):
    n = len(datos)
    posicion = k * (n + 1) / 4

    if posicion.is_integer():
        return datos[int(posicion) - 1]
    else:
        parte_entera = int(posicion)
        parte_decimal = posicion - parte_entera

        inferior = datos[parte_entera - 1]
        superior = datos[parte_entera]

        return inferior + parte_decimal * (superior - inferior)


media = sum(numeros) / len(numeros)
mediana = calcular_mediana(numeros)

q1 = calcular_cuartil(numeros, 1)
q2 = calcular_cuartil(numeros, 2)
q3 = calcular_cuartil(numeros, 3)

IQR = q3 - q1


limite_inferior = q1 - 1.5 * IQR
limite_superior = q3 + 1.5 * IQR





print("\n=== RESULTADOS ===")
print("Promedio:", media)
print("Mediana:", mediana)
print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)

print("\nIQR:", IQR)
print("Límite inferior:", limite_inferior)
print("Límite superior:", limite_superior)




def graficos_comparados(numeros, q1, mediana, q3):
    import matplotlib.pyplot as plt

    plt.figure()

    #Línea
    plt.subplot(1, 2, 1)

    valores = [min(numeros), q1, mediana, q3, max(numeros)]
    labels = ["Min", "Q1", "Mediana", "Q3", "Max"]
    
    plt.plot(valores, marker='o')
    plt.xticks(range(len(labels)), labels)

    plt.axhline(limite_inferior, linestyle=':', label="Límite inferior")
    plt.axhline(limite_superior, linestyle=':', label="Límite superior")

    plt.title("Resumen estadístico")
    plt.ylabel("Valores")
    plt.legend()
    plt.grid()

    # Boxplot
    plt.subplot(1, 2, 2)

    plt.boxplot(numeros)
    plt.title("Boxplot")
    plt.grid()

    plt.tight_layout()
    plt.show()


graficos_comparados(numeros, q1, mediana, q3)    


