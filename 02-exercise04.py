import numpy as np

T = np.array([20, 25, 30, 35, 40])

F = (9 * T)/5 + 32

print (F)

fehrenheit_mean = np.mean(F)
print(fehrenheit_mean)

###one check : for 20, F = (9 * 20)/5 + 32 = 68