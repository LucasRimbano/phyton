from sympy import symbols, sympify, diff

# Variables
x, y = symbols('x y')

print("Regla de la cadena: dz/dx = dz/dy * dy/dx\n")

# Ingreso de funciones
z = sympify(input("Ingresá z en función de y (ej: y**2 + 3*y): "))
y_expr = sympify(input("Ingresá y en función de x (ej: x**2 + 1): "))

# Derivadas
dz_dy = diff(z, y)
dy_dx = diff(y_expr, x)

# Regla de la cadena
dz_dx = dz_dy.subs(y, y_expr) * dy_dx

# Resultados
print("\n--- RESULTADOS ---")
print("dz/dy =", dz_dy)
print("dy/dx =", dy_dx)
print("dz/dx =", dz_dx)