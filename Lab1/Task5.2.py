import numpy as np
import matplotlib.pyplot as plt

fs = 500          
f = 10            
A = 5             
duration = 1.0    

t = np.arange(0, duration, 1/fs)

clean_signal = A * np.sin(2 * np.pi * f * t)

noise = 0.25 * np.random.randn(len(t))

noisy_signal = clean_signal + noise

plt.plot(t, clean_signal, label="Clean Signal")
plt.plot(t, noisy_signal, label="Noisy Signal", alpha=0.7)

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("10 Hz Signal with Gaussian Noise")
plt.legend()
plt.grid(True)
plt.savefig("Task4_2.png")
plt.show()
