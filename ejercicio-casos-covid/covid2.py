#Parte 1. Cargar la base de datos y explorar su estructura
#(a) ¿Cuántas filas y columnas tiene la base de datos?
#(b) ¿Qué tipo de datos hay?
#(c)¿Hay columnas con valores nulos?
#(d) ¿Cuál es el rango de fechas de los datos?
#e) ¿Qué provincias están incluidas?

import pandas as pd     
import numpy as np 
import matplotlib.pyplot as plt 


df = pd.read_csv("Covid19Argentina.csv")
df["Testing_Date"]= pd.to_datetime(df["Testing_Date"])

print(df)
filas,columnas = df.shape
print(df.dtypes)
print(df.isnull().sum())
fechaminima = df["Testing_Date"].min()
print(fechaminima)
fechamaxima = df["Testing_Date"].max()
print(fechamaxima)
print("Las provincias incluidas son:",df["Province"].unique())

# Análisis de los casos confirmados
#(a) ¿Cuántos casos confirmados hay por provincia?
casos_por_provincia = df.groupby('Province')['Positive_Cases'].sum()
print("Casos confirmados por provincia:")
print(casos_por_provincia)


casos_por_dia =df.groupby("Testing_Date")["Positive_Cases"].sum()

#(b) Hacer un gráfico de la evolución de los casos confirmados en función del tiempo.

plt.figure()
plt.plot(casos_por_dia.index, casos_por_dia.values)

plt.xlabel("Fecha")
plt.ylabel("Casos positivos")
plt.title("Evolución de casos de COVID en Argentina")


plt.tight_layout()
plt.savefig("grafico.png")
plt.show()

#c) ¿Cuál fue el día con mayor cantidad de casos positivos reportados?



#primero nmesesito hacer la cantidad de casos por dia




#ahora cuento maximo 

dia_max = casos_por_dia.idxmax()
max_casos = casos_por_dia.max()

print(f"La fecha con más casos es: {dia_max}")
print(f"La cantidad de casos fue de: {max_casos}")



#menor casos

dia_min = casos_por_dia.idxmin()
min_casos = casos_por_dia.min()


print(f"La fecha con menos casos es: {dia_min}")
print(f"La cantidad de casos fue de: {min_casos}")

#e) ¿Qué diferencia observas entre los casos positivos detectados en los distintos tipos de instituciones de salud?
casos_por_tipo = df.groupby("Type")["Positive_Cases"].sum()

print("Casos positivos por tipo de institución:")
print(casos_por_tipo)
