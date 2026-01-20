import numpy as np
import matplotlib.pyplot as plt

fs = 500          
f = 10          
A = 5             
duration = 1.0   

t = np.arange(0, duration, 1/fs)

x = A * np.sin(2 * np.pi * f * t)

plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("10 Hz Sinusoid (A=5, fs=500 Hz)")
plt.grid(True)
plt.show()
