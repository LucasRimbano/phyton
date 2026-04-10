import pandas as pd

df = pd.DataFrame({
    "Nombre": ["Ana", "Juan", "Pedro", "Luis", "Sofi"],
    "Curso": ["Python", "Python", "Java", "Python", "Java"],
    "Nota": [8, 6, 9, 7, 10]
})

print("DATAFRAME ORIGINAL:")
print(df)
print()

print("SUMA DE NOTAS POR CURSO:")
print(df.groupby("Curso")["Nota"].sum())
print()

print("PROMEDIO DE NOTAS POR CURSO:")
print(df.groupby("Curso")["Nota"].mean())
print()

print("CANTIDAD DE ALUMNOS POR CURSO:")
print(df.groupby("Curso")["Nota"].count())
print()

print("NOTA MÁXIMA POR CURSO:")
print(df.groupby("Curso")["Nota"].max())
print()