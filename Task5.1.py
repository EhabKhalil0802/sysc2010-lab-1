import numpy as np
import matplotlib.pyplot as plt

# Given specs
fs = 500          # sampling frequency (Hz)
f = 10            # signal frequency (Hz)
A = 5             # amplitude
duration = 1.0    # seconds

# Time vector: 1 second of samples at 500 Hz -> 500 samples
t = np.arange(0, duration, 1/fs)

# 10 Hz sinusoid
x = A * np.sin(2 * np.pi * f * t)

# Plot
plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("10 Hz Sinusoid (A=5, fs=500 Hz)")
plt.grid(True)
plt.show()
