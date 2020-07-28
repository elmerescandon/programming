import rotaciones as r
import numpy as np
from serialrobot import *


# d, th, a, alppha
L = [[2.95,   np.pi/2,      0,  np.pi/2, 'r'],
     [0,      np.pi/2,   2.30,        0, 'r'],
     [0,        np.pi,  -0.50,  np.pi/2, 'r'],
     [2.70,     np.pi,      0,  np.pi/2, 'r'],
     [0,     -np.pi/2,      0,  np.pi/2, 'r'],
     [0.70,         0,      0,        0, 'r']]
r6 = SerialRobot(L, name='r6')
q = np.deg2rad(np.array([0, 0, 0, 0, 0, 30]))
r6.plot(q, ascale=0.3, ee=False)
\
