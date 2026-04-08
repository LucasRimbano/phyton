import numpy as np


n = int(input("Ingresá el tamaño de la matriz (ej: 2 para 2x2, 3 para 3x3): "))


print("\n--- Cargando matriz A ---")
A = []
for i in range(n):
    fila = []
    for j in range(n):
        valor = float(input(f"A[{i}][{j}]: "))
        fila.append(valor)
    A.append(fila)

print("\n--- Cargando matriz B ---")
B = []
for i in range(n):
    fila = []
    for j in range(n):
        valor = float(input(f"B[{i}][{j}]: "))
        fila.append(valor)
    B.append(fila)


A = np.array(A)
B = np.array(B)

print("\n--- Elegí la operación ---")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")

opcion = int(input("Opción: "))


if opcion == 1:
    resultado = A + B
    print("\nResultado (Suma):")
    print(resultado)

elif opcion == 2:
    resultado = A - B
    print("\nResultado (Resta):")
    print(resultado)

elif opcion == 3:
    resultado = A @ B
    print("\nResultado (Multiplicación):")
    print(resultado)

else:
    print("Opción inválida")