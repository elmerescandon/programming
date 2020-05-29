import sympy as sp
from sympy.matrices import Matrix
import numpy as np
import rotaciones as r


sp.init_printing()
q1, q2, l1, l2 = sp.symbols(r'q_1 q_2 l_1 l_2')

T01 = r.strotz(q1)*r.strasl(l1, 0, 0)
T12 = r.strotz(q2)*r.strasl(l2, 0, 0)
T = sp.simplify(T01*T12)

z0 = Matrix([[0], [0], [1]])
p0 = Matrix([[0], [0], [0]])
z1 = T01[0:3, 2]
p01 = T01[0:3, 3]
p02 = T[0:3, 3]
Jv1 = r.crossproduct(z0, p02-p0)
Jv2 = r.crossproduct(z1, p02-p01)
Jw1 = z0
Jw2 = z1

J_q1 = Matrix.vstack(Jv1, Jw1)
J_q2 = Matrix.vstack(Jv2, Jw2)
J_geom = Matrix.hstack(J_q1, J_q2)
print("Jacobiano Geométrico de RR:")
display(J_geom)
print("Rango de la Matriz Jacobiana:{}".format(Matrix.rank(J_geom)))
