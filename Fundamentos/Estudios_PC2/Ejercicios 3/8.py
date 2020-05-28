import rotaciones as r
import sympy as sp
from sympy.matrices import Matrix
import numpy as np
from serialrobot import *
#d,th,a ,alpha


def sdh(d, theta, a, alpha):

    T = Matrix([[sp.cos(theta), -sp.cos(alpha)*sp.sin(theta), sp.sin(alpha)*sp.sin(theta), a*sp.cos(theta)],
                [sp.sin(theta),  sp.cos(alpha)*sp.cos(theta), -
                 sp.sin(alpha)*sp.cos(theta), a*sp.sin(theta)],
                [0,                      sp.sin(alpha),            sp.cos(alpha),            d],
                [0,                               0,                     0,            1]])

    return T


q1, q2, q3, l1, px, py, pz, l3, ax, ay, az = sp.symbols('q1 q2 q3 l1 px py pz l3 ax ay az')
sp.init_printing()
T1 = sdh(0, sp.pi/2+q1, 0, sp.pi/2)
T2 = sdh(0, sp.pi/2+q2, l1, 0)
T3 = sdh(0, q3, 0, sp.pi/2)
T03 = sp.simplify(T1*T2)
pw = Matrix([[px-l3*ax],
             [py-l3*ay],
             [pz-l3*az],
             [1]])
p32 = Matrix([[0],
              [0],
              [l3],
              [1]])


pas = sp.simplify(pw*p32.pinv())
pas
