# Examen Final 2019-1
# Fundamentos de Robótica
# Pregunta 3
# ==================================
# %%Inicializar librerías
import symbolic as sym
import numeric as num
import sympy as sp
import numpy as np
from sympy.matrices import Matrix
sp.init_printing()

# %% Especificaciones del cuadrotor
w = sp.symbols(r'w')
m = 1  # kg
g = 9.81
kf = 5.5 * 1e-6
dr2c = 0.2  # Distancia del rotor al centro

f = kf*w  # Fuerza generada por el rotor
peso = m * np.array([[0],[0],[-g]])

# %% Pregunta 1
r_acc = np.array([[0],[0],[0.1]])  # Aceleración requerida
F_tot = (m*r_acc - peso)/(kf*4)
print(np.round(np.sqrt(F_tot),2))
# Rpta:671.16 rad/s

# %% Pregunta 2
r_acc_2 = np.array([[0],[0],[0]])  # Aceleración requerida
F_tot_2 = (m*r_acc_2 - peso)/(kf*4)
print(np.round(np.sqrt(F_tot_2),2))
# Rpta: 667.76 rad/s

# %% Pregunta 3
m,g,theta,w1,w2,w3,w4,kf = sp.symbols(r'm g \theta w_1 w_2 w_3 w_4 k_f')
R_x = sym.srot(theta,'x')
peso = m*Matrix([[0],[0],[-g]])
f_1 = (w1**2)*kf
f_2 = (w2**2)*kf
f_3 = (w3**2)*kf
f_4 = (w4**2)*kf
fuerzas = Matrix([[0],[0],[f_1 + f_2 + f_3 + f_4]])
equ = sp.simplify(R_x*fuerzas)
display(equ)
