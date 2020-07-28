# %% Inicializar librerías
import numeric as num
import symbolic as sym
import numpy as np
import sympy as sp

# %% Inicializar variables
sin = sp.sin
cos = sp.cos

q1,l1,q2,d = sp.symbols(r'q_1 l_1 q_2 d')
T02 = sym.strot(q1,'z')*sym.strasl(l1,0,0)*sym.strot(sp.pi/4,'z')*sym.strasl(q2-d,0,0)
m1,m2 = sp.symbols(r'm_1 m_2')

I1,I2 = sp.symbols(r'I_1 I_2')
I_1 = sp.Matrix([[0,0,0],
                 [0,0,0],
                 [0,0,I1]])
I_2 = sp.Matrix([[0,0,0],
                 [0,0,0],
                 [0,0,I2]])
# Posición del centro de masa
CoM_1 = sp.Matrix([[cos(q1)*(l1/2)],
                   [sin(q1)*(l1/2)],
                   [0]])
CoM_2 = T02[0:3,3]

# Matriz de rotación para los eslabones con respecto al sistema inercial
R_1 = sym.strot(q1,'z')[0:3,0:3]
R_2 = T02[0:3,0:3]

# Jacobianos de velocidades lineales
Jv_1 = sp.Matrix([[-sin(q1)*(l1/2),0],
                  [cos(q1)*(l1/2),0],
                  [0,0]])

Jv_2 = sp.Matrix([[-l1*sin(q1) - (q2-d)*sin(q1+sp.pi/4),cos(q1+sp.pi/4)],
                  [l1*cos(q1) + (q2-d)*cos(q1+sp.pi/4),sin(q1+sp.pi/4)],
                  [0,0]])

# Jacobianos de velocidades angulares
Jw_1 = sp.Matrix([[0,0],
                  [0,0],
                  [1,0]])

Jw_2 = sp.Matrix([[0,0],
                  [0,0],
                  [1,0]])

# Calcular la matriz de masa
CoM = [CoM_1,CoM_2]
Jv = [Jv_1,Jv_2]
Jw = [Jw_1,Jw_2]
R = [R_1,R_2]
m = [m1, m2]
I = [I_1, I_2]

mass = sym.Mass_Matrix(Jv,Jw,R,m,I)

# Parte E - %%
fz = sp.symbols(r'f_z')
J1 = sp.Matrix.vstack(Jv_1,Jw_1)
F = sp.Matrix([[0],[0],[fz],[0],[0],[0]])
t = J1.T*F
display(t)
