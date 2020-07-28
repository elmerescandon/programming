# %% Inicializar librerías
import numeric as num
import symbolic as sym
import numpy as np
import sympy as sp

# %% Inicializar variables
cos = sp.cos
sin = sp.sin
# Articulacioones y constantes
q1,d2 = sp.symbols(r'q_1 d_2')
q1_dot,d2_dot = sp.symbols(r'\dot{q_1} \dot{d_2}')
l1 = sp.symbols(r'l_1')
m1,m2 = sp.symbols(r'm_1 m_2')
Ixx1,Ixy1,Ixz1,Iyx1,Iyy1,Iyz1,Izx1,Izy1,Izz1 = sp.symbols(r'I_{xx_1} I_{xy_1} I_{xz_1} I_{yx_1} I_{yy_1} I_{yz_1} I_{zx_1} I_{zy_1} I_{zz_1}')
I_1 = sp.Matrix([[Ixx1,Ixy1,Ixz1],
                [Iyx1,Iyy1,Iyz1],
                [Izx1,Izy1,Izz1]])

Ixx2,Ixy2,Ixz2,Iyx2,Iyy2,Iyz2,Izx2,Izy2,Izz2 = sp.symbols(r'I_{xx_2} I_{xy_2} I_{xz_2} I_{yx_2} I_{yy_2} I_{yz_2} I_{zx_2} I_{zy_2} I_{zz_2}')
I_2 = sp.Matrix([[Ixx2,Ixy2,Ixz2],
                [Iyx2,Iyy2,Iyz2],
                [Izx2,Izy2,Izz2]])

# Centros de Masa
CoM_1 = sp.Matrix([[cos(q1)*(l1/2)],
                   [sin(q1)*(l1/2)],
                   [0]])

CoM_2 = sp.Matrix([[cos(q1)*l1],
                   [sin(q1)*l1],
                   [d2]])

# Matriz de Rotación
R_1 = sp.Matrix([[cos(q1),-sin(q1),0],
                 [sin(q1),cos(q1),0],
                 [0,0,1]])
R_2 = R_1

# Jacobiano de velocidad lineal
Jv_1 = sp.Matrix([[-sin(q1)*(l1/2),0],
                  [cos(q1)*(l1/2),0],
                  [0,0]])

Jv_2 = sp.Matrix([[-sin(q1)*l1,0],
                  [cos(q1)*l1,0],
                  [0,1]])

# Jacobiano de velocidad angular
Jw_1 = sp.Matrix([[0,0],
                  [0,0],
                  [1,0]])
Jw_2 = Jw_1

Jv = [Jv_1, Jv_2]
Jw = [Jw_1, Jw_2]
m = [m1,m2]
R = [R_1,R_2]
CoM = [CoM_1,CoM_2]
I = [I_1,I_2]
q = [q1,d2]
qdot = [q1_dot,d2_dot]
Mass = sym.Mass_Matrix(Jv,Jw,R,m,I)
display(Mass)
Coriolis = sym.Coriolis_Matrix(Mass,qdot,q)
display (Coriolis)
