import rotaciones as r
import sympy as sp
from sympy.matrices import Matrix
import numpy as np
from serialrobot import *
#d,th,a ,alpha

L = [[0,     0, 0.2,  -np.pi/2,  'r'],
     [0, np.pi,   0,   np.pi/2, 'p'], ]
robo7 = SerialRobot(L, name='robot7')
T = robo7.fkine([-0.6435011087932845, -3.6], verbose=False)
print(np.round(T, 3))


# Cinemática Inversa Analítica del sistema RP

xd = np.array([-2, -3])
q2 = np.sqrt(xd[0]**2 + xd[1]**2 - (0.2)**2)

if (np.arctan2(xd[1], xd[0]) < 0):
    q2 = -q2

cq1 = (0.2*xd[0] + q2*xd[1])/(0.2**2 + q2**2)
sq1 = (1/q2)*(0.2*cq1 - xd[0])
q1 = np.arctan2(sq1, cq1)
print(q1)
print(q2)
