import matplotlib.pyplot as plt
from matplotlib_venn import venn3

total = 50
futbol = 28
basquet = 20
tenis = 18
futbol_basquet = 8
futbol_tenis = 7
basquet_tenis = 6
tres = 3

solo_futbol = futbol - (futbol_basquet - tres) - (futbol_tenis - tres) - tres
solo_basquet = basquet - (futbol_basquet - tres) - (basquet_tenis - tres) - tres
solo_tenis = tenis - (futbol_tenis - tres) - (basquet_tenis - tres) - tres

solo_futbol_basquet = futbol_basquet - tres
solo_futbol_tenis = futbol_tenis - tres
solo_basquet_tenis = basquet_tenis - tres

al_menos_uno = (
    solo_futbol + solo_basquet + solo_tenis +
    solo_futbol_basquet + solo_futbol_tenis +
    solo_basquet_tenis + tres
)

ninguno = total - al_menos_uno

print("=== RESULTADOS ===")
print(f"Solo fútbol: {solo_futbol}")
print(f"Solo básquet: {solo_basquet}")
print(f"Solo tenis: {solo_tenis}")
print(f"Fútbol y Básquet solamente: {solo_futbol_basquet}")
print(f"Fútbol y Tenis solamente: {solo_futbol_tenis}")
print(f"Básquet y Tenis solamente: {solo_basquet_tenis}")
print(f"Los tres: {tres}")
print(f"Al menos uno: {al_menos_uno}")
print(f"Ninguno: {ninguno}")

plt.figure()
venn3(
    subsets=(
        solo_futbol,          # 100
        solo_basquet,         # 010
        solo_futbol_basquet,  # 110
        solo_tenis,           # 001
        solo_futbol_tenis,    # 101
        solo_basquet_tenis,   # 011
        tres                  # 111
    ),
    set_labels=("Fútbol", "Básquet", "Tenis")
)

plt.title("Diagrama de Venn - Deportes")
plt.show()