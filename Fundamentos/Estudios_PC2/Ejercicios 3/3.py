import rotaciones as r
import sympy as sp
from sympy.matrices import Matrix
import numpy as np
from serialrobot import *


def sdh(theta, d, a, alpha):

    T = Matrix([[sp.cos(theta), -sp.cos(alpha)*sp.sin(theta), sp.sin(alpha)*sp.sin(theta), a*sp.cos(theta)],
                [sp.sin(theta),  sp.cos(alpha)*sp.cos(theta), -
                 sp.sin(alpha)*sp.cos(theta), a*sp.sin(theta)],
                [0,                      sp.sin(alpha),            sp.cos(alpha),            d],
                [0,                               0,                     0,            1]])

    return T


q1, q2, q3, l1, l2 = sp.symbols('q1 q2 q3 l1 l2')
sp.init_printing()
T1 = sdh(q1, 0, l1, sp.pi/2)
T2 = sdh(q2, 0, l2, 0)
T3 = sdh(q3, 0, 0, 0)
T = sp.simplify(T1*T2*T3)
T

# Plot de robot serial
l1 = 1
l2 = 1
L = [[0, 0, l1, np.pi/2, 'r'],
     [0, 0, l2,       0, 'r'],
     [0, 0, 0,        0, 'r']]
robo3 = SerialRobot(L, name='robo3')
T = robo3.fkine([0, 0, 0], verbose=False)
print(np.round(T, 3))

alims = [[-2, 2], [-2, 2], [-0.2, 1.3]]
robo3.plot([0, 0, 0], axlimits=alims)
