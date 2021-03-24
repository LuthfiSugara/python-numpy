import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

#stacking matrix / menumpuk matrix

c = np.hstack((a,b))
print(c)

d = np.vstack((a,b))
print(d)

mat1 = np.zeros((2,3))
mat2 = np.ones((2,3))
mat3 = np.hstack((mat1, mat2))
print(mat3)