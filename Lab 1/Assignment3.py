# Assignment 3: Working with Sound Files
import simpleaudio as sa
from scipy.io import wavfile as wav
import numpy as np
import soundfile as sf

# Part A
wav1 = sa.WaveObject.from_wave_file('train32.wav')
fs1, y1 = wav.read('train32.wav')
channels1 = wav1.num_channels
print("y1 Sampling rate = ", fs1)
print("y1 Number of channels = ", channels1)
print("y1 wave type = ", y1.dtype)

wav2 = sa.WaveObject.from_wave_file('tuba11.wav')
fs2, y2 = wav.read('tuba11.wav')
channels2 = wav2.num_channels
print("y2 Sampling rate = ", fs2)
print("y2 Number of channels = ", channels2)
print("y2 wave type = ", y2.dtype)

# Part B
play_obj_1 = wav1.play()
play_obj_1.wait_done()

play_obj_2 = wav2.play()
play_obj_2.wait_done()

play_obj_1_new = sa.play_buffer(y1, 1, 2, fs2)
play_obj_1_new.wait_done()

play_obj_2_new = sa.play_buffer(y2, 2, 2, fs1)
play_obj_2_new.wait_done()

# Part C
len1 = len(y1)
len2 = len(y2)
print("length of the first signal = ", len1)
print("length of the second signal = ", len2)

y3 = y2[0:len1]
len_y3 = len(y3)
print("length of the y3 = ", len_y3)

y4 = y3[:,0] + y1
play_y4 = sa.play_buffer(y4, 1, 2, fs1)
play_y4.wait_done()

# Part D
pause = np.zeros(int(4*fs2))
y5 = np.concatenate([y1, pause, y2[:,0]])
play_y5 = sa.play_buffer(y5, 1, 2, fs1)
sf.write('Assignment3PartD.wav', y5, fs1)
play_y5.wait_done()
