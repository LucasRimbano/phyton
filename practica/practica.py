import numpy as np


a = np.array([2, 4, 6, 8, 10, 12])
b = np.arange(1, 7)
c = np.linspace(0, 5, 6)

print( a[1:4])


print( a.sum())
print( a.mean())
print( a.max())
print( a.min())

a[2] = 99
print("a modificado:", a)

m1 = b.reshape(2, 3)
m2 = np.array([[1, 2, 3],
               [4, 5, 6]])

print("m1:")
print(m1)

print("m2:")
print(m2)

print("m1 + m2:")
print(m1 + m2)

print("m1 * m2:")
print(m1 * m2)


x = np.array([[1, 2],
              [3, 4]])

y = np.array([[2, 0],
              [1, 2]])

print("x @ y:")
print(x @ y)
print("y dot x puede serrrr sadasda:")
print(y.dot(x))

print("shape de a:", a.shape)
print("shape de m1:", m1.shape)

print("Transpuesta de m2:")
print(m2.T)


print("Elementos de a mayores que 8:")
print(a[a > 8])


d = a[1:4]
e = a.copy()

d[0] = 500
e[1] = 700

print("a después de modificar d:", a)
print("d:", d)
print("e:", e)