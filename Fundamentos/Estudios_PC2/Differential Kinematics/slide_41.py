import sympy as sp
from sympy.matrices import Matrix
import numpy as np
import rotaciones as r


q3, q1, q2, d = sp.symbols(r'q_3 q_1 q_2 d')
fk = Matrix([[q3*sp.cos(q2)*sp.cos(q1)],
             [q3*sp.cos(q2)*sp.sin(q1)],
             [d + q3*sp.sin(q2)]])
q = Matrix([q1, q2, q3])


J = fk.jacobian(q)
J
