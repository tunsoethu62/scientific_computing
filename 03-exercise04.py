import numpy as np

a = np.arange(0, 16, 3)
b = np.linspace(0, 1, 6)

print (a)
print (b)

assert a.shape == (6, ) and b.shape == (6, )
print ("Verified!")