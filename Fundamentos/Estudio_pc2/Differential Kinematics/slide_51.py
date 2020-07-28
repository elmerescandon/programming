import sympy as sp
from sympy.matrices import Matrix
import numpy as np
import rotaciones as r


# Simbólico
q1, q2, q3 = sp.symbols(r'q_1 q_2 q_3')
l1 = 0.5
l2 = 1
l3 = 0.5
sfk_rrr = Matrix([[l1*sp.cos(q1) + l2*sp.cos(q1+q2) + l3*sp.cos(q1+q2+q3)],
                  [l1*sp.sin(q1) + l2*sp.sin(q1+q2) + l3*sp.sin(q1+q2+q3)],
                  [q1 + q2 + q3]])

sq = Matrix([q1, q2, q3])
sJa = sfk_rrr.jacobian(sq)
Ja_1 = sJa.subs({q1: sp.pi/4, q2: -sp.pi/4, q3: -sp.pi/4})
Ja_inv = sp.simplify(Ja_1.inv())
Ja_inv
twist = Matrix([[0.7],
                [0],
                [0]])
q_deseado = sp.simplify(Ja_inv*twist)
Ja_1
q_deseado
