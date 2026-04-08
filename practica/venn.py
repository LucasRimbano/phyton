import matplotlib.pyplot as plt
from matplotlib_venn import venn2


total = 50
basquet = 30
voley = 25
ambos = 10


solo_basquet = basquet - ambos
solo_voley = voley - ambos
ninguno = total - (solo_basquet + solo_voley + ambos)

print("=== RESULTADOS ===")
print(f"Solo básquet: {solo_basquet}")
print(f"Solo vóley: {solo_voley}")
print(f"Ambos: {ambos}")
print(f"Ninguno: {ninguno}")


plt.figure()
venn2(subsets=(solo_basquet, solo_voley, ambos),
      set_labels=('Básquet', 'Vóley'))

plt.title("Diagrama de Venn - Deportes")
plt.show()