# ==================================
# %%Inicializar librerías
import symbolic as sym
import numeric as num
import sympy as sp
import numpy as np
from sympy.matrices import Matrix
sp.init_printing()

# %% Obtención de Centros de Masa
q1,l1,d2,q2 = sp.symbols(r'q_1 l_2 d_2 q_2')
m1,m2 = sp.symbols(r'm_1 m_2')
T = sym.strot(q1,'z')*sym.strasl(l1,0,0)*sym.strot(sp.pi/4,'z')

CoM_1 = Matrix([[(l1/2)*sp.cos(q1)],[(l1/2)*sp.sin(q1)],[0]])

CoM_2 = Matrix([[l1*sp.cos(q1)+(q2-d2)*sp.cos(sp.pi/4 + q1)],[l1*sp.sin(q1)+(q2-d2)*sp.sin(sp.pi/4 + q1)],[0]])

Jv1 = Matrix([[-(l1/2)*sp.sin(q1),0],[(l1/2)*sp.cos(q1),0],[0,0]])
Jw1 = Matrix([[0,0],[0,0],[1,0]])

Jv2 = Matrix([[-l1*sp.sin(q1)-(q2-d2)*sp.sin(sp.pi/4+q1),sp.cos(sp.pi/4+q1)],[l1*sp.cos(q1)+(q2-d2)*sp.cos(sp.pi/4+q1),sp.sin(sp.pi/4+q1)],[0,0]])
Jw2 = Matrix([[0,0],[0,0],[1,0]])

I1,I2 = sp.symbols(r'I_1 I_2')
I_1 = Matrix([[0,0,0],[0,0,0],[0,0,I2]])

I_2 = Matrix([[0,0,0],[0,0,0],[0,0,I1]])

Jv = [Jv1,Jv2]
Jw = [Jw1,Jw2]
m = [m1,m2]
Inercia = [I_1,I_2]
R0 = Matrix([[1,0,0],
             [0,1,0],
             [0,0,1]])
R1 = Matrix([[1,0,0],
             [0,1,0],
             [0,0,1]])
R = [R0,R1]

M = sym.Mass_Matrix(Jv,Jw,R,m,Inercia)
display(sp.simplify(M))
