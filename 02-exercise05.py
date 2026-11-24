import numpy as np

t = np.array([0,1,2,3,4,5])
x0 = 2
v = 3
x = x0 + (v * t)
print (x)

dx = x[5] - x[0]
print (f"distance travelled: {dx}")

assert dx == 15
print ("Verification successful.")

#final position just give us the coordinate of the position of the robot. Displacement means distance travelled by the robot between two time frames.