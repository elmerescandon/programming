import numpy as np
import sympy as sp

A = np.array([[0,0,0,0,0,1],
              [3125,625,125,25,5,1],
              [0,0,0,0,1,0],
              [3125,500,75,10,1,0],
              [0,0,0,1,0,0],
              [2500,300,30,2,0,0]])

b = np.array([[0],[1],[0],[0],[0],[0]])

print(np.linalg.inv(A).dot(b))
