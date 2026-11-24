import math

theta_zero = 15

omega = 30

t = 2.5

theta = theta_zero + (omega * t)

print (f"Final angle: {theta}.")

assert math.isclose(theta, 90)
print ("Calculation verified.")