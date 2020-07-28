# %% Inicializar librerías
import numeric as num
import symbolic as sym
import numpy as np
import sympy as sp

# %% Creación de valores
q1,q2,q3,d1,d2,L2 = sp.symbols(r'q_1 q_2 q_3 d_1 d_2 L_2')
m1,m2,m3 = sp.symbols(r'm_1 m_2 m_3')

# Matrices Inerciales
# Matrices de inercial con respecto al sistema del CoM
Ixx1,Ixy1,Ixz1,Iyx1,Iyy1,Iyz1,Izx1,Izy1,Izz1 = sp.symbols(r'I_{xx_1} I_{xy_1} I_{xz_1} I_{yx_1} I_{yy_1} I_{yz_1} I_{zx_1} I_{zy_1} I_{zz_1}')
I1 = sp.Matrix([[Ixx1,Ixy1,Ixz1],
                [Iyx1,Iyy1,Iyz1],
                [Izx1,Izy1,Izz1]])

Ixx2,Ixy2,Ixz2,Iyx2,Iyy2,Iyz2,Izx2,Izy2,Izz2 = sp.symbols(r'I_{xx_2} I_{xy_2} I_{xz_2} I_{yx_2} I_{yy_2} I_{yz_2} I_{zx_2} I_{zy_2} I_{zz_2}')
I2 = sp.Matrix([[Ixx2,Ixy2,Ixz2],
                [Iyx2,Iyy2,Iyz2],
                [Izx2,Izy2,Izz2]])

Ixx3,Ixy3,Ixz3,Iyx3,Iyy3,Iyz3,Izx3,Izy3,Izz3 = sp.symbols(r'I_{xx_3} I_{xy_3} I_{xz_3} I_{yx_3} I_{yy_3} I_{yz_3} I_{zx_3} I_{zy_3} I_{zz_3}')
I3 = sp.Matrix([[Ixx3,Ixy3,Ixz3],
                [Iyx3,Iyy3,Iyz3],
                [Izx3,Izy3,Izz3]])

# Centros de Masa
CoM_1 = sp.Matrix([[0],[q1],[0]])

T_01_com = sym.strasl(0,q1+d1,0)*sym.strot(q2,'z')*sym.strasl(d2,0,0)
CoM_2 = T_01_com[0:3,3]

T_02_com = sym.strasl(0,q1+d1,0)*sym.strot(q2,'z')*sym.strasl(L2,q3,0)
CoM_3 = T_02_com[0:3,3]
display(CoM_3)

# Matrices de rotación
R1 = sp.eye(3)
R2 = T_01_com[0:3,0:3]
R3 = T_02_com[0:3,0:3]

# Jacobiano de velocidad lineal
Jv1 = sp.Matrix([[0,0,0],
                 [1,0,0],
                 [0,0,0]])

Jv2 = sp.Matrix([[0,-d2*sp.sin(q2),0],
                 [1,d2*sp.cos(q2),0],
                 [0,0,0]])

Jv3 = sp.Matrix([[0,-L2*sp.sin(q2) - q3*sp.cos(q2),-sp.sin(q2)],
                 [1,L2*sp.cos(q2)-q3*sp.sin(q2),sp.cos(q2)],
                 [0,0,0]])

# Jacobiano de velocidad angular
Jw1 = sp.zeros(3,3)
Jw2 = sp.Matrix([[0,0,0],
                 [0,0,0],
                 [0,1,0]])
Jw3 = sp.Matrix([[0,0,0],
                 [0,0,0],
                 [0,1,0]])

Jv = [Jv1,Jv2,Jv3]
Jw = [Jw1,Jw2,Jw3]
I = [I1,I2,I3]
R = [R1,R2,R3]
m = [m1,m2,m3]
mass = sym.Mass_Matrix(Jv,Jw,R,m,I)
display(sp.simplify(mass))
