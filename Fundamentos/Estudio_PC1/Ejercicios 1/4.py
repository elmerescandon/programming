import numpy as np

Rab = np.array([[1,   0,    0],
                [0, 0.5,  -np.sqrt(3)/2],
                [0, np.sqrt(3)/2, 0.5]])

Rac = np.array([[0,  0,  -1],
                [0,  1,   0],
                [1,  0,   0]])

Rbc = Rab.T.dot(Rac)
print(Rbc)
