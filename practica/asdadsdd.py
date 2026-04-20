import numpy as np 

a = np.array([[1, 2], [4,3], [7,6]])
b = np.array([[2,0], [1,3]]) 
c = np.array([5,4,1])
d = np.array([10,20])


result2 = a @ b

result4 = a @ d
result5 = a * d
result6 = c @ a
print(result2)

print("el resultado de 4 no se peujde : " + str(result4))
print(result5)
print(result6)