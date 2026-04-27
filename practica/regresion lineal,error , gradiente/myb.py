     #   Dada una regresión lineal 𝑦 = 𝑚𝑥 + 𝑏 Dar las derivadas parciales del error cuadrático respecto
      #  a las variables m y b.

from sympy import symbols, Function, Sum, diff

m, b, i, n = symbols('m b i n')
x, y = symbols('x y', cls=Function)

sum_of_squares = Sum((m*x(i) + b - y(i))**2, (i, 0, n))

d_m = diff(sum_of_squares, m)
d_b = diff(sum_of_squares, b)

print("Error cuadrático:", sum_of_squares)
print("Derivada parcial respecto a m:", d_m)
print("Derivada parcial respecto a b:", d_b)