# Assignment 2: Amplitude Operations on Signals
import numpy as np
# Part A
fs = 2
Ts = 1/fs
t = np.arange(0, 3.1, Ts)
x = 0.5 * t
y = t ** 2
print("x = ", x)
print("y = ", y)
# Part B
z = x - 2 * y
print("z = ", z)
# Part C
index = np.where(t == 2)
w1 = z[index]
print("w1 = ", w1[0])
# Part D
index2 = np.where((t >= 0) & (t <= 1.5))
print(index2)
w2 = z[index2]
print("w2 = ", w2)
