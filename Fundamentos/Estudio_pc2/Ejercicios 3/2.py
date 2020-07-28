import numpy as np
import sympy as sp
from sympy.matrices import Matrix
import rotaciones as r

# Funciones simbólicas para tener valores


def strot(ang, a):
    if (a == 'y'):
        T = Matrix([[sp.cos(ang),  0, sp.sin(ang), 0],
                    [0,            1,           0, 0],
                    [-sp.sin(ang), 0, sp.cos(ang), 0],
                    [0,            0,           0, 1]])
    elif (a == 'z'):
        T = Matrix([[sp.cos(ang), -sp.sin(ang), 0, 0],
                    [sp.sin(ang),  sp.cos(ang), 0, 0],
                    [0,                      0, 1, 0],
                    [0,                      0, 0, 1]])
    elif(a == 'x'):
        T = Matrix([[1,           0,            0, 0],
                    [0, sp.cos(ang), -sp.sin(ang), 0],
                    [0, sp.sin(ang),  sp.cos(ang), 0],
                    [0,           0,            0, 1]])
    return T


def strasl(a):
    T = Matrix([[1, 0, 0, a],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
    return T


q1, q2, q3, l1, l2, l3 = sp.symbols("q1 q2 q3 l1 l2 l3")
sp.init_printing()
T_01 = strot(-q1, 'y')*strasl(l1)
T_12 = strot(-q2, 'y')*strasl(l2)
T_23 = strot(-q3, 'y')*strasl(l3)
T_03 = sp.simplify(T_01*T_12*T_23)
T_03
