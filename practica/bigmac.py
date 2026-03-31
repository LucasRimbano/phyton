import pandas as pd     
import numpy as np 
from collections import defaultdict
import matplotlib.pyplot as plt

df = pd.read_excel("C:\\Users\\lucas\\OneDrive\\Desktop\\phyton\\BigMacIndex25 (1).xlsx")

print(df.columns) 


costo_medio = df["dollar_price"].mean()
print("El costo medio de la Big Mac es de: ",costo_medio)


Q1 = df["dollar_price"].quantile(0.25)
Q3 = df["dollar_price"].quantile(0.75)

IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

valores_atipicos = df[(df["dollar_price"] < limite_inferior) | (df["dollar_price"] > limite_superior)]

print("Valores atípicos:")
print(valores_atipicos)




def mode(values):
    counts = defaultdict(lambda: 0)

    for s in values:
        counts[s] += 1

    max_count = max(counts.values())
    modes = [v for v in set(values) if counts[v] == max_count]
    return modes


df["dollar_price"].std()
print("La desviación estándar del precio de la Big Mac es de: ", df["dollar_price"].std())



plt.hist(df["dollar_price"], bins=10)


plt.xlabel("Precio del Big Mac (USD)")
plt.ylabel("Cantidad de países")
plt.title("Distribución del precio del Big Mac en distintos países")

plt.show()