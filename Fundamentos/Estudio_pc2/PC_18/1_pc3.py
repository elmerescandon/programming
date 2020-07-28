import numpy as np
import sympy as sp
import rotaciones as r
from serialrobot import *

q1, q2, q3, l1, l2, l3 = sp.symbols(r'q_1 q_2 q_3 l_1 l_2 l_3')


# Pregunta 1 - PC3 - 2018-1

# Parte 1
T01 = r.sdh(0, q1, l1, 0)
T12 = r.sdh(0, q2, -l2, sp.pi/2)
T23 = r.sdh(l3, q3, 0, 0)
T = sp.simplify(T01*T12*T23)
z0 = Matrix([[0], [0], [1]])
p0 = Matrix([[0], [0], [0]])

Jv1 = r.crossproduct(z0, T[0:3, 3]-p0)
Jw1 = z0
J1 = Matrix.vstack(Jv1, Jw1)

Jv2 = r.crossproduct(z0, T[0:3, 3]-T01[0:3, 3])
Jw2 = T01[0:3, 2]  # z1 representada dentro T01
J2 = Matrix.vstack(Jv2, Jw2)

T02 = T01*T12
Jv3 = r.crossproduct(z0, T[0:3, 3]-T02[0:3, 3])
Jw3 = T02[0:3, 2]
J3 = Matrix.vstack(Jv3, Jw3)

J_geom = Matrix.hstack(J1, J2)
J_geom = Matrix.hstack(J_geom, J3)
J_geom

# Part 2
twist = Matrix([[0], [0], [0], [0], [0], [1]])
J_geom_sub = J_geom.subs({q1: 0, q2: sp.pi, q3: sp.pi, l1: 1, l2: 1, l3: 1})
q_d = J_geom_sub.pinv()*twist
q_d
