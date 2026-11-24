import numpy as np

x = np.array([5, 10, 15, 20])
y = np.zeros ((3,4))
z = np.ones((2,3), dtype=int)

print (x)
print (y)
print (z)

assert y.shape == (3,4) and z.shape == (2,3)
print ("Verified!")