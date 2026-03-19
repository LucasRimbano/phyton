#primero multiplica matrices y dps combino con el vector 
from numpy import array

# Transformacion 1
i_hat1 = array([0, 1])
j_hat1 = array([-1, 0])
transform1 = array([i_hat1, j_hat1]).transpose()

# Transformacion 2
i_hat2 = array([1, 0])
j_hat2 = array([1, 1])
transform2 = array([i_hat2, j_hat2]).transpose()

# Combino Transformaciones
combined = transform2 @ transform1

print(i_hat1)
print(i_hat2)
print("TRANSFOR 1")
print(transform1)
print("TRANSFORM 2")
print(transform2)

# Test
print("COMBINED MATRIX:\n {}".format(combined))

# Aplico al vector v
v = array([1, 2])

print(combined.dot(v))