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

#Total_Tests


casos_por_provincia = df.groupby('Province')['Positive_Cases'].sum()

print("Casos confirmados por provincia:")
print(casos_por_provincia)

#(b) Hacer un gráfico de la evolución de los casos confirmados en función del tiempo.


#primero nmesesito hacer la cantidad de casos por dia






