import matplotlib.pyplot as plt
from matplotlib_venn import venn2

total = 40
matematica = 22
fisica = 18
ambos = 9

solo_matematica = matematica - ambos
solo_fisica = fisica - ambos
ninguno = total - (solo_matematica + solo_fisica + ambos)

print("=== RESULTADOS ===")
print(f"Solo Matemática: {solo_matematica}")
print(f"Solo Física: {solo_fisica}")
print(f"Ambos: {ambos}")
print(f"Ninguno: {ninguno}")

plt.figure()
venn2(subsets=(solo_matematica, solo_fisica, ambos),
      set_labels=('Matemática', 'Física'))

plt.title("Diagrama de Venn - Materias")
plt.show()