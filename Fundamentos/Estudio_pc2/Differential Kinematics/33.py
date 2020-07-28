import sympy as sp
from sympy.matrices import Matrix
import numpy as np
import rotaciones as r


q1, q2, q3, q4, L = sp.symbols(r'q_1 q_2 q_3 q_4 L')
DH = [[0, q1, 0, sp.pi/2, 'r'],
      [0, q2, 0, sp.pi/2, 'r'],
      [L, q3, 0, sp.pi/2, 'r'],
      [0, q4, L, 0, 'r']]


def jacob_g(DH):
    T_ref = []  # Matriz que almacena los valores de T
    T = Matrix([[1, 0, 0, 0],  # Inicializar Matriz de trasnformacion
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
    z0 = Matrix([[0], [0], [1]])
    p0 = Matrix([[0], [0], [0]])
    J = Matrix([])
    for i in range(len(DH)):
        Ti = sp.simplify(r.sdh(DH[i][0], DH[i][1], DH[i][2], DH[i][3]))
        T = T*Ti
        T_ref.append(T)

    for n in range(len(DH)):
        if (n == 0):
            z = z0
            p = p0
        else:
            z = T_ref[n-1][0:3, 2]
            p = T_ref[n-1][0:3, 3]

        if (DH[i][4] == 'r'):
            Jv = r.crossproduct(z, T_ref[len(DH)-1][0:3, 3] - p)
            Jw = z

        elif (DH[i][4] == 'p'):
            Jv = z
            Jw = 0
        J1 = sp.Matrix.vstack(Jv, Jw)
        J = sp.Matrix.hstack(J, J1)
    return T_ref, sp.simplify(J)


a, J = jacob_g(DH)
Js = J.subs({q1: 0, q2: 135*sp.pi/180, q3: sp.pi, q4: sp.pi})
Js
