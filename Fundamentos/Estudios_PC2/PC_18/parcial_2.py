import sympy as sp
import numpy as np
from sympy.matrices import Matrix
import rotaciones as r
from serialrobot import *


q1, q2, q3, d1, a2, a3 = sp.symbols(r'q_1 q_2 q_3 d_1 a_2 a_3')

# T01 = r.sdh(d1, q1, 0, sp.pi/2)
# T12 = r.sdh(0, q2, a2, 0)
# T23 = r.sdh(0, q3, a3, 0)
# T = T01*T12*T23
# z0 = Matrix([[0], [0], [1]])
# p0 = Matrix([[0], [0], [0]])
# Jv1 = r.crossproduct(z0, T[0:3, 3]-p0)
# Jw1 = z0
# J1 = sp.simplify(Matrix.vstack(Jv1, Jw1))
#
# Jv2 = r.crossproduct(T01[0:3, 2], T[0:3, 3]-T01[0:3, 3])
# Jw2 = T01[0:3, 2]
# J2 = sp.simplify(Matrix.vstack(Jv2, Jw2))
#
# T02 = T01*T12
# Jv3 = r.crossproduct(T02[0:3, 2], T[0:3, 3]-T02[0:3, 3])
# Jw3 = T02[0:3, 2]
# J3 = sp.simplify(Matrix.vstack(Jv3, Jw3))
# J = Matrix.hstack(Matrix.hstack(J1, J2), J3)

DH = [[d1, q1, 0, sp.pi/2, 'r'],
      [0, q2, a2, 0, 'r'],
      [0, q3, a3, 0, 'r']]
L = [[1, 0, 0, np.pi/2, 'r'],
     [0, 0, 1, 0, 'r'],
     [0, 0, 1, 0, 'r']]
rrr = SerialRobot(L, name='rrr')
rrr.plot([0, 0, 0])

T, J = r.jacob_g(DH)
J
# Inciso 2
J_s = J.subs({d1: 1, a2: 1, a3: 1, q1: 0, q2: 0, q3: 0})
J_s
twist = Matrix([[1], [0], [0], [0], [0], [0]])
# J_s_inv = J_s.pinv()

q = J_s.pinv()*twist
q


F = Matrix([[0], [1], [-1], [1], [1], [1]])
t = J_s.T*F
t
