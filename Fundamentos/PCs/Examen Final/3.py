# Examen Final 2020-1
# Fundamentos de Robótica
# Elmer Raúl Escandón Tufino
# ==================================
# %%Inicializar librerías
import symbolic as sym
import sympy as sp
import numpy as np
import numeric as num

## Pregunta 2
q1,q2,q3,l2,l1 = sp.symbols(r'q_1 q_2 q_3 l_2 l_1')
qd_1,qd_2,qd_3 = sp.symbols(r'\dot{q_1} \dot{q_2} \dot{q_3}')
T02 = sym.strot(q1,'z')*sym.strasl(0,0,q2)*sym.strot(sp.pi/2,'x')*sym.strot(q3,'z')*sym.strasl(l2,0,0)
m1,m2,m3 = sp.symbols(r'm_1 m_2 m_3')

# Matrices de inercial con respecto al sistema del CoM
Ixx1,Ixy1,Ixz1,Iyx1,Iyy1,Iyz1,Izx1,Izy1,Izz1 = sp.symbols(r'I_{xx_1} I_{xy_1} I_{xz_1} I_{yx_1} I_{yy_1} I_{yz_1} I_{zx_1} I_{zy_1} I_{zz_1}')
I_1 = sp.Matrix([[Ixx1,Ixy1,Ixz1],
             [Iyx1,Iyy1,Iyz1],
             [Izx1,Izy1,Izz1]])

Ixx2,Ixy2,Ixz2,Iyx2,Iyy2,Iyz2,Izx2,Izy2,Izz2 = sp.symbols(r'I_{xx_2} I_{xy_2} I_{xz_2} I_{yx_2} I_{yy_2} I_{yz_2} I_{zx_2} I_{zy_2} I_{zz_2}')
I_2 = sp.Matrix([[Ixx2,Ixy2,Ixz2],
             [Iyx2,Iyy2,Iyz2],
             [Izx2,Izy2,Izz2]])

Ixx3,Ixy3,Ixz3,Iyx3,Iyy3,Iyz3,Izx3,Izy3,Izz3 = sp.symbols(r'I_{xx_3} I_{xy_3} I_{xz_3} I_{yx_3} I_{yy_3} I_{yz_3} I_{zx_3} I_{zy_3} I_{zz_3}')
I_3 = sp.Matrix([[Ixx3,Ixy3,Ixz3],
             [Iyx3,Iyy3,Iyz3],
             [Izx3,Izy3,Izz3]])



CoM_1 = sp.Matrix([[0],[0],[0]])
CoM_2 = sp.Matrix([[0],[0],[q2-l1]])
CoM_3 = T02[0:3,3]

# Matrices de rotacion para los eslabones
R1 = sp.eye(3)
R2 = sym.strot(q1,'z')[0:3,0:3]
R3 = T02[0:3,0:3]

# Jacobianos de velocidad
Jv_1 = sp.eye(3)
Jv_2 = sp.Matrix([[0,0,0],
                  [0,0,0],
                  [0,1,0]])
Jv_3 = sp.Matrix([[-l2*sp.cos(q3)*sp.sin(q1),0,-l2*sp.cos(q1)*sp.sin(q3)],
                  [l2*sp.cos(q3)*sp.cos(q1),0,-l2*sp.sin(q1)*sp.sin(q3)],
                  [0,1,l2*sp.cos(q3)]])

# Jacobianos de Velocididad angular
Jw_1 = sp.Matrix([[0,0,0],
                  [0,0,0],
                  [1,0,0]])
Jw_2 = sp.Matrix([[0,0,0],
                  [0,0,0],
                  [1,0,0]])
Jw_3 = sp.Matrix([[0,0,sp.sin(q1)],
                  [0,0,-sp.cos(q1)],
                  [1,0,0]])

# Calcular la matriz de masa
CoM = [CoM_1,CoM_2,CoM_3]
Jv = [Jv_1,Jv_2,Jv_3]
Jw = [Jw_1,Jw_2,Jw_3]
R = [R1,R2,R3]
m = [m1,m2,m3]
I = [I_1, I_2,I_3]

mass = sym.Mass_Matrix(Jv,Jw,R,m,I)
display(sp.simplify(mass))

q_dots = [qd_1,qd_2,qd_3]
qs = [q1,q2,q3]
cor = sym.Coriolis_Matrix(mass,q_dots,qs)
display(sp.simplify(cor))
