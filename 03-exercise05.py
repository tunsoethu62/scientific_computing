import numpy as np

theta_zero = 10
theta_final = 100
T = 3

# w = (theta_final - theta_zero)/T = (100 - 10)/3 = 30
w = (theta_final - theta_zero)/T

t = np.linspace(0, 3, 7)
theta = theta_zero + w * t

print (f"time: {t}")
print (f"angles: {theta}")

assert theta[0] == 10 and theta[6] == 100
print ("Verified!")