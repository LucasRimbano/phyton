

# Ejemplo:
# Una fábrica compra papas a 2 proveedores.
# Proveedor 1: se compra 5/6 del total, rechazo 20%
# Proveedor 2: se compra 1/6 del total, rechazo 10%

# Probabilidades iniciales
p_prov1 = 5/6
p_prov2 = 1/6

# Probabilidades condicionales
p_rechazo_dado_prov1 = 0.20
p_rechazo_dado_prov2 = 0.10

# Complementarias
p_no_rechazo_dado_prov1 = 1 - p_rechazo_dado_prov1
p_no_rechazo_dado_prov2 = 1 - p_rechazo_dado_prov2

# -----------------------------
# 1) PROBABILIDADES DE LAS RAMAS
# -----------------------------
rama_prov1_y_rechazo = p_prov1 * p_rechazo_dado_prov1
rama_prov1_y_no_rechazo = p_prov1 * p_no_rechazo_dado_prov1

rama_prov2_y_rechazo = p_prov2 * p_rechazo_dado_prov2
rama_prov2_y_no_rechazo = p_prov2 * p_no_rechazo_dado_prov2

print("=== PROBABILIDADES DE LAS RAMAS ===")
print(f"P(Proveedor 1 y rechazo) = {rama_prov1_y_rechazo:.4f}")
print(f"P(Proveedor 1 y no rechazo) = {rama_prov1_y_no_rechazo:.4f}")
print(f"P(Proveedor 2 y rechazo) = {rama_prov2_y_rechazo:.4f}")
print(f"P(Proveedor 2 y no rechazo) = {rama_prov2_y_no_rechazo:.4f}")

# -----------------------------
# 2) PROBABILIDAD TOTAL
# -----------------------------
p_rechazo = rama_prov1_y_rechazo + rama_prov2_y_rechazo
p_no_rechazo = rama_prov1_y_no_rechazo + rama_prov2_y_no_rechazo

print("\n=== PROBABILIDAD TOTAL ===")
print(f"P(Rechazo) = {p_rechazo:.4f}")
print(f"P(No rechazo) = {p_no_rechazo:.4f}")

# -----------------------------
# 3) BAYES
# -----------------------------
# Queremos: si una papa fue rechazada, ¿probabilidad de que sea del proveedor 1?
p_prov1_dado_rechazo = rama_prov1_y_rechazo / p_rechazo
p_prov2_dado_rechazo = rama_prov2_y_rechazo / p_rechazo

print("\n=== TEOREMA DE BAYES ===")
print(f"P(Proveedor 1 | rechazo) = {p_prov1_dado_rechazo:.4f}")
print(f"P(Proveedor 2 | rechazo) = {p_prov2_dado_rechazo:.4f}")