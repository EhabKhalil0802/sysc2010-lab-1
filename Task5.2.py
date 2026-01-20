import numpy as np
import matplotlib.pyplot as plt

# Given specs
fs = 500          # sampling frequency (Hz)
f = 10            # signal frequency (Hz)
A = 5             # amplitude
duration = 1.0    # seconds

# Time vector
t = np.arange(0, duration, 1/fs)

# Clean 10 Hz sinusoid
clean_signal = A * np.sin(2 * np.pi * f * t)

# Generate Gaussian noise (mean=0, var=1)
noise = 0.25 * np.random.randn(len(t))

# Noisy signal
noisy_signal = clean_signal + noise

# Plot both signals
plt.plot(t, clean_signal, label="Clean Signal")
plt.plot(t, noisy_signal, label="Noisy Signal", alpha=0.7)

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("10 Hz Signal with Gaussian Noise")
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig("Task4_2.png")
plt.show()
