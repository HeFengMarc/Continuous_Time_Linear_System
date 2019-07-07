# Assignment 1: Creating the  Manipulating Arrays
import numpy as np
# Part A
y1 = np.array([4, 6, 2])
# Part B
ca = y1[1]
cb = y1[1:3]
d = len(y1)
print(ca)
print(cb)
print(d)
# Part C
x1 = 2 * np.ones(5)
x2 = np.arange(-2, 3, 1)
print(x1)
print(x2)
# Pard D
arrp = x1 + x2
arrc = np.concatenate([x1, x2])
print(arrp)
print(arrc)
