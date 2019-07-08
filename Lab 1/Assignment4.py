# Assignment 4: Plotting Comparisons
# Put 'conda install matplotlib' as the input if you are using the
# Mac OS system.
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# Part A
fs = 5
Ts = 1/fs
t = np.arange(-2, 4.1, Ts)
w = np.abs(t)
print(t)
print("w = ", w)
x = 2 - t
print("x = ", x)
y = -0.5*(t**2)
print("y = ", y)

# Part B
fig1 = plt.figure(1)
plt.plot(t, w, label = 'w(t)')
plt.plot(t, x, label = 'x(t)')
plt.plot(t, y, label = 'y(t)')
plt.xlabel('t')
plt.title('Comparison Plot')
plt.grid()
plt.legend()
plt.show()
