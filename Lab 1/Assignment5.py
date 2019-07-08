# Assignment 5: Plotting Sound Files in Subplots
from scipy.io import wavfile as wav
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Part A
fs1, y1 = wav.read('train32.wav')
fs2, y2 = wav.read('tuba11.wav')
Ts1 = 1/fs1
Ts2 = 1/fs2
t1 = np.arange(0, len(y1) * Ts1, Ts1)
t2 = np.arange(0, len(y2) * Ts2 - 0.1 * Ts2, Ts2)
msec_t1 = t1 * 1000
msec_t2 = t2 * 1000

# Part B
fig1 = plt.figure(1)
fig1.subplots_adjust(hspace=0.8, wspace=0.3)

plt.subplot(2,1,1)
plt.plot(msec_t1, y1)
plt.xlim(-50, 2500)
plt.ylim(-35000, 35000)
plt.xlabel('t1 (msec)')
plt.ylabel('y1(t1)')
plt.title('y1 vs. t1')

plt.subplot(2,1,2)
plt.plot(msec_t2, y2[:,1])
plt.xlim(-50,2500)
plt.ylim(-35000, 35000)
plt.xlabel('t2 (msec)')
plt.ylabel('y2(t2)')
plt.title('y2 vs. t2')

plt.show()
