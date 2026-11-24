import math
r = 0.05
w = 8
t = 10

d = r * w * t

print (f"Distance travelled: {d}")

assert math.isclose(d, 4)
print ("Calculation completed")

#scientific computing mainly concerns with creating mathematical models and implementing them in the code

#computer mainly stores data in binary finite numbers. So, storing floating points is not exact, just approximation.