import pandas as pd
import matplotlib.pyplot as plt


datos = {
    "Notas": [4, 6, 7, 8, 5, 9, 10, 6, 7, 8, 9, 5, 6, 7, 8]
}

df = pd.DataFrame(datos)

print("Base de datos:")
print(df)

print("\nEstadísticas:")
print(df.describe())


plt.figure()
plt.boxplot(df["Notas"])
plt.title("Boxplot de Notas")
plt.ylabel("Notas")
plt.grid()

plt.show()