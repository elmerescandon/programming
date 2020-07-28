# Examen Final 2020-1
# Fundamentos de Robótica
# Elmer Raúl Escandón Tufino
# ==================================
# %%Inicializar librerías
import symbolic as sym
import sympy as sp
import numpy as np
from serialrobot import *



# %% Pregunta 1: Robot de GDL
# Parámetros de Denavit-Hartenberg para cada articulación
# Orden de los parámetros: d, th, a, alpha. Articulaciones: 'r' (revolución), 'p' (prismática)
l2 = 40#0.4
l3 = 30#0.3
q1 = 0; q3=0;q4=0
q2 = 30;q5=30
L = [[  0,  q1,0,     0, 'r'],
     [  q2, 0, 0,     np.pi/2, 'p'],
     [  0,  q3,l2,     np.pi, 'r'],
     [  0,  q4,l3, np.pi/2, 'r'],
     [q5,np.pi/2,0,0,'p']]

scara = SerialRobot(L, name='scara')
T = scara.fkine([0,0,0,0,0], verbose=False)
print(np.round(T,3))

# alims = [[-2,2],[-2,2],[-0.2, 1.3]]
scara.plot([0, 0, 0, 0,0])
