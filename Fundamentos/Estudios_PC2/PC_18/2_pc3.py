import sympy as sp
import numpy as np
from sympy.matrices import Matrix
import rotaciones as rots

q1, q2, q3, d2, d3 = sp.symbols(r'q_1 q_2 q_3 d_2 d_3')

# Jacobian geometrico de la velocidad
s = sp.sin
c = sp.cos
pi = sp.pi
Jg_p = Matrix([[-s(q1)*s(q2)*d3 - c(q1)*d2, c(q1)*c(q2)*d3, c(q1)*s(q2)],
               [c(q1)*s(q2)*d3 - s(q1)*d2, s(q1)*c(q2)*d3, s(q1)*s(q2)],
               [0,      -s(q2)*d3,       c(q2)]])

Jg_w = Matrix([[0, -sp.sin(q1), 0],
               [0, sp.cos(q1), 0],
               [1, 0, 0]])


Jg = Matrix.vstack(Jg_p, Jg_w)
Jg

# Inciso D
r, p, y, dr, dp, dy = sp.symbols(r'\phi_r \phi_p \phi_y \dot{\phi_r} \dot{\phi_p} \dot{\phi_y}')

# Rz = rots.srot(r, 'z')
# Ry = rots.srot(p, 'y')
# Rx = rots.srot(y, 'x')
#
# R = sp.simplify(Rz*Ry*Rx)
# R_dot = sp.simplify(R.diff(r)*dr + R.diff(p)*dp + R.diff(y)*dy)
# w_skew = sp.simplify(R_dot*R.T)
# sp.simplify(w_skew)
# w = rots.skew2vec(w_skew)

E = Matrix([[1, 0, 0, 0,         0,                    0],
            [0, 1, 0, 0,         0,                    0],
            [0, 0, 1, 0,         0,                    0],
            [0, 0, 0, 0, -sp.sin(r), sp.cos(p)*sp.cos(r)],
            [0, 0, 0, 0,  sp.cos(r), sp.cos(p)*sp.sin(r)],
            [0, 0, 0, 1,          0,          -sp.sin(p)]])


J_a = E.inv()*Jg
qs = Matrix([[q1], [q2], [q3]])

Jgprueba = E*J_a
sp.simplify(Jgprueba)
