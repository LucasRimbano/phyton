import pandas as pd
import matplotlib.pyplot as plt


datos = {
    "Notas": [5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 30]
}

df = pd.DataFrame(datos)
sorted_df = df.sort_values(by="Notas")
print("Datos ordenados:")


print("\nEstadísticas:")


plt.figure()
plt.boxplot(df["Notas"])
plt.title("Boxplot de Notas")
plt.ylabel("Notas")
plt.grid()

plt.show()