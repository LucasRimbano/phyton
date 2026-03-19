import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt





df = pd.read_csv("Covid19Argentina.csv")
print(df)

filas, columnas = df.shape
print("La cantidad de filas es de: " ,filas)
print("La cantidad de columnas es de: ",columnas)
print(df.dtypes)
print(df.isnull().sum())



fecha_min = df["Testing_Date"].min()
fecha_max = df["Testing_Date"].max()

print("La fecha minima es de:" ,fecha_min)
print("La fecha maxima es de:" ,fecha_max)
print("Las provincias incluidas son:",df["Province"].unique())

#parte 2
df_confirmados = df[df["Province"].str.lower() == "Positive_Cases"]

casos_por_provincia = df_confirmados.groupby("Province").size()

print("Casos confirmados por provincia:")
print(casos_por_provincia)

casos_por_dia = df.groupby("Testing_Date")["Positive_Cases"].sum()

dia_max_Casos = casos_por_dia.idxmax()
cantidad_Max = casos_por_dia.max()

print("El dia con mas casos fue:",dia_max_Casos)
print("La cantidad maxima decasos es fue:",cantidad_Max)


dia_min_casos = casos_por_dia.idxmin()
cantidad_Min = casos_por_dia.min()

print("El dia con menos casos fue:",dia_min_casos)
print("La cantidad minima de casos fue:",cantidad_Min)

casos_por_tipo = df.groupby("Type")["Positive_Cases"].sum()

print("Casos positivos por tipo de institución:")
print(casos_por_tipo)




plt.figure()
plt.plot(casos_por_dia)


plt.title("Evolución de casos positivos COVID-19")
plt.xlabel("Fecha")
plt.ylabel("Cantidad de casos")

plt.xticks(rotation=45)  
plt.tight_layout()
plt.show()