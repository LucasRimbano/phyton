
import pandas as pd     
import numpy as np 
import matplotlib.pyplot as plt 


df = pd.read_csv("Covid19Argentina.csv")
df["Testing_Date"]= pd.to_datetime(df["Testing_Date"])

print(df)
filas,columnas = df.shape
# Análisis de los casos confirmados
#(a) ¿Cuántos casos confirmados hay por provincia?
casos_por_provincia = df.groupby('Province')['Positive_Cases'].sum()
print("Casos confirmados por provincia:")
print(casos_por_provincia)