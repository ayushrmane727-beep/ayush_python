import numpy as np
arr=np.linspace(1,25,25)
b=arr.reshape(5,5)
print(b)
c=np.diag(b)
print(c)
d=np.diag(np.fliplr(b))
print(d)
e=arr.T
print(e)
a=b[1:4,1:4]
print(a)
