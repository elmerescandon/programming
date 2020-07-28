import numpy as np
import sympy as sp
import rotaciones as r


q1, q2, q3, d1 = sp.symbols(r'q_1 q_2 q_3 d_1')

L = [[d1, q1, 0, 0, 'r'],
     [q2, 0, 0, -sp.pi/2, 'r'],
     [q3, 0, 0, 0, 'r']]

T, J_g = r.jacob_g(L)
J_v = J_g[0:3, 0:3]
J_w = J_g[3:6, 0:3]
(J_g.T*J_g).det()
