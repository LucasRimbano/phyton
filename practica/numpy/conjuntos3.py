import matplotlib.pyplot as plt
from matplotlib_venn import venn3

total = 60
netflix = 32
disney = 26
prime = 24
netflix_disney = 12
netflix_prime = 10
disney_prime = 9
tres = 4

solo_netflix_disney = netflix_disney - tres
solo_netflix_prime = netflix_prime - tres
solo_disney_prime = disney_prime - tres

solo_netflix = netflix - solo_netflix_disney - solo_netflix_prime - tres
solo_disney = disney - solo_netflix_disney - solo_disney_prime - tres
solo_prime = prime - solo_netflix_prime - solo_disney_prime - tres

al_menos_una = (
    solo_netflix +
    solo_disney +
    solo_prime +
    solo_netflix_disney +
    solo_netflix_prime +
    solo_disney_prime +
    tres
)

ninguna = total - al_menos_una

print("=== RESULTADOS ===")
print(f"a) Solo Netflix: {solo_netflix}")
print(f"b) Solo Disney+: {solo_disney}")
print(f"c) Solo Prime Video: {solo_prime}")
print(f"d) Netflix y Disney+ solamente: {solo_netflix_disney}")
print(f"e) Netflix y Prime Video solamente: {solo_netflix_prime}")
print(f"f) Disney+ y Prime Video solamente: {solo_disney_prime}")
print(f"g) Al menos una: {al_menos_una}")
print(f"h) Ninguna: {ninguna}")

plt.figure()
venn3(
    subsets=(
        solo_netflix,          # 100
        solo_disney,           # 010
        solo_netflix_disney,   # 110
        solo_prime,            # 001
        solo_netflix_prime,    # 101
        solo_disney_prime,     # 011
        tres                   # 111
    ),
    set_labels=("Netflix", "Disney+", "Prime Video")
)

plt.title("Diagrama de Venn - Plataformas de Streaming")
plt.show()