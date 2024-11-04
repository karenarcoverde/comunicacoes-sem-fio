import numpy as np
import matplotlib.pyplot as plt

# Distance range in kilometers
distances = np.linspace(1, 20, 100)
distances_m = distances * 1000  # convert distances from km to meters
# Okumura-Hata model constants
hb = 30  # base station antenna height in meters
hm = 3   # mobile station antenna height in meters
fc = 1e3  # carrier frequency in MHz (1000 MHz)

# Okumura-Hata path loss (Urban areas)
PL_oh = 69.55 + 26.16 * np.log10(fc) - 13.82 * np.log10(hb) - 3.2 * (np.log10(11.75 * hm))**2 + 4.97 + (44.9 - 6.55 * np.log10(hb)) * np.log10(distances)

# Free-space path loss
PL_fs = 32.44 + 20 * np.log10(distances_m)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(distances, PL_oh, label='Okumura-Hata Path Loss', color='b', linewidth=2)
plt.plot(distances, PL_fs, label='Free-Space Path Loss', color='g', linestyle='--', linewidth=2)

# Labels and title
plt.xlabel('Distance (km)')
plt.ylabel('Path Loss (dB)')
plt.title('Comparison of Okumura-Hata and Free-Space Path Loss Models')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()


