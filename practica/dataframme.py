import pandas as pd

df = pd.DataFrame({
    "Provincia": ["Buenos Aires", "Córdoba", "Buenos Aires", "Córdoba", "Mendoza"],
    "Casos": [10, 5, 7, 8, 3]
})


casos_x_provincia = df.groupby("Provincia")["Casos"].sum()
print(casos_x_provincia)