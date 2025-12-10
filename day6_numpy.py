import numpy as np
matrix = np.array([
    [10,20,30],
    [40,50,60]
])
print("\nMatrix:\n",matrix)
print("shape:",matrix.shape)
print("Rows:",matrix.shape[0])
print("columns:",matrix.shape[1])

print("Row-wise Sum:", np.sum(matrix,axis=1))
print("column-wise Sum:", np.sum(matrix,axis=0))
