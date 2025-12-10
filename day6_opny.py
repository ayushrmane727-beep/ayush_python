import numpy as np
matrix =np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
c=matrix.shape
a=np.sum(matrix,axis=1)
b=np.sum(matrix,axis=0)
print(matrix)
print(a)
print(b)
print(c)
print(matrix[1,:])
print(matrix[:,2])
print(matrix[0:2,1:3])