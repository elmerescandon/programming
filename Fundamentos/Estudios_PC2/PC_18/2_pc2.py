import sympy as sp
import numpy as np
import rotaciones as r
from serialrobot import *
# (a)

# Primer joint es de revolución
# Segundo joint es prismático
# Tercer joint es prismático


# (b)
q1, q2, q3, d1 = sp.symbols(r'q_1 q_2 q_3 d_1')
T01 = r.sdh(0, q1, d1, -sp.pi/2)
T12 = r.sdh(q2, -sp.pi/2, 0, -sp.pi/2)
T23 = r.sdh(q3, sp.pi/2, 0, -sp.pi/2)
T = T01*T12*T23
T


# c
px, py = sp.symbols(r'p_x p_y')

A = Matrix([[-sp.sin(q1), sp.cos(q1)],
            [sp.cos(q1), sp.sin(q1)]])

p = Matrix([[px - d1*sp.cos(q1)],
            [py - d1*sp.sin(q1)]])

qs = A.inv()*p
sp.simplify(qs)
