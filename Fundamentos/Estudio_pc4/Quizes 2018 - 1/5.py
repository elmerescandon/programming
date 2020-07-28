# Examen Final 2019-1
# FundamenPtos de Robótica
# Pregunta 3
# ==================================
# %%Inicializar librerías
import numeric as num
import symbolic as sym
import sympy as sp
import numpy as np
from sympy.matrices import Matrix
sp.init_printing()

# %% Pregunta 1 - Paso 1: Obtención de centros de masa

# Matriz de trasnformación de 0 a 2
q1,q2,l1,d1,d2 = sp.symbols(r'q_1 q_2 l_1 d_1 d_2')

T0_2 = sym.strot(q1,'z')*sym.strasl(0,0,l1)*sym.strot(sp.pi/2,'y')*sym.strot(sp.pi/2,'z')*sym.strot(q2,'z')
CoM_1 = Matrix([[0],[0],[d1]])
CoM_2 = (T0_2*Matrix([[d2],[0],[0],[1]]))[0:3,0]
CoM = [CoM_1,CoM_2]
display(CoM)

# %% Paso 2: Obtención de jacobiano lineal y angular
qs = [q1,q2]
axis_0 = Matrix([[0],[0],[1]])
axis_1 = T0_2[0:3,2]
axis = [axis_0,axis_1]
Jv = sym.linear_velocity_CoM(CoM,qs,axis,['r','r'])
Jw = sym.angular_velocity_CoM(CoM,axis,['r','r'])
display(Jv)
display(Jw)

# %% Paso 3: Calcular la matriz de Masa
m1, m2 = sp.symbols('m_1 m_2')
R_01 = T0_2[0:3,0:3]
R0 = sym.srot(q1,'z')
m = [m1,m2]
R = [R0,R_01]
Ixx1,Iyy1,Izz1 = sp.symbols(r'I_{xx_1} I_{yy_1} I_{zz_1}')
I1 = Matrix([[Ixx1,0,0],
             [0,Iyy1,0],
             [0,0,Izz1]])

Ixx2,Iyy2,Izz2 = sp.symbols(r'I_{xx_2} I_{yy_2} I_{zz_2}')
I2 = Matrix([[Ixx2,0,0],
             [0,Iyy2,0],
             [0,0,Izz2]])

I = [I1,I2]
Mass = sym.Mass_Matrix(Jv,Jw,R,m,I)
display(sp.simplify(Mass))
