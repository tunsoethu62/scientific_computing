import numpy as np
import math

x = np.array([2,4,6,8,10])

y = (3*x) + 5

print (y)

assert np.array_equal(y, np.array([11, 17, 23, 29, 35]))
print ("Correct")