import sympy as sp
from sympy.matrices import Matrix
import numpy as np
import rotaciones as r
import matplotlib.pyplot as plt
from serialrobot import *


# l1, l2, l3, l4 = sp.symbols(r'l_1 l_2 l_3 l_4')
l1 = 1
l2 = 3
l3 = 3
l4 = 1
L = [[l1, np.pi/2, 0, np.pi/2, 'r'],
     [0, 0, l2, 0, 'r'],
     [0, 0, l3, 0, 'r'],
     [0, 0, 0, np.pi/2, 'r'],
     [l4, np.pi/2, 0, 0, 'r']]

r5 = SerialRobot(L, name='r5')
r5.plot([0, 0, 0, 0, 0])
