import numpy as np

R = np.array([[1,   0,    0],
              [0, 0.6,  0.8],
              [0, -0.8, 0.6]])
bp = np.array([[2],
               [4],
               [5]])
ap = R.T.dot(bp)
bbp = R.dot(ap)
print(ap)
print(bbp)
