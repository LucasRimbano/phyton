
import pandas as pd
import numpy as np 


np.random.seed(42)
materias = ["Matemática", "Historia", "Biología", "Física", "Lengua"]
notas = np.random.randint(1, 11, size=(100, 5))
df = pd.DataFrame(notas, columns=materias)
df["Promedio"] = df.mean(axis=1)
print(df.head())


reprobados = (df[materias] < 6).sum(axis=1)
print("Cantidad de alumnos que reprobaron >= 2 materias:", (reprobados >= 2).sum())

# Top 5 mejores promedios
top5 = df.sort_values(by="Promedio", ascending=False).head(5)
print("Top 5 mejores promedios:")
print(top5)
