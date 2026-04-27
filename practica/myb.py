import pandas as pd
from sympy import *

# Importar puntos desde CSV
points = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())

m, b, i, n = symbols('m b i n')
x, y = symbols('x y', cls=Function)

sum_of_squares = Sum((m*x(i) + b - y(i)) ** 2, (i, 0, n))

d_m = diff(sum_of_squares, m) \
    .subs(n, len(points) - 1).doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)

d_b = diff(sum_of_squares, b) \
    .subs(n, len(points) - 1).doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)

# Compilar usando lambdify
d_m = lambdify([m, b], d_m)
d_b = lambdify([m, b], d_b)

# Modelo inicial
m = 0.0
b = 0.0

L = 0.001
iterations = 100_000

for i in range(iterations):
    old_m = m
    old_b = b

    m -= d_m(old_m, old_b) * L
    b -= d_b(old_m, old_b) * L

print(f"y = {m}x + {b}")
