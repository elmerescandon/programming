from rotaciones import *
import numpy as np
import sympy as sp

R = np.array([[0,-1,0],
              [0,0,1],
              [-1,0,0]])

q = quaterion(R)
print(q)
w = 0.5
ex = -0.5
ey = 0.5
ez = 0.5
