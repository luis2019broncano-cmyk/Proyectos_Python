import numpy as np
import matplotlib.pyplot as plt

# Datos simulados para una carga inductiva (como un motor)
R = 100  # Resistencia en Ohms
L = 0.5  # Inductancia en Henrios
f = 60   # Frecuencia en Hz
XL = 2 * np.pi * f * L

Z = complex(R, XL) # Impedancia compleja: $Z = R + jX_L$

print(f"Impedancia Simulada: {Z.real:.2f} + {Z.imag:.2f}j Ω")

# Graficar vector
plt.quiver(0, 0, Z.real, Z.imag, angles='xy', scale_units='xy', scale=1, color='r')
plt.xlim(0, R*1.5); plt.ylim(0, XL*1.5); plt.grid(True)
plt.title("Simulacion de Impedancia Compleja")
plt.show()