import numpy as np
import rotaciones as r

pb = np.array([[2], [4], [5], [1]])

Tb_a = np.array([[1, 0, 0, 2],
                 [0, 0.6, 0.8, -1],
                 [0, -0.8, 0.6, 1],
                 [0, 0, 0, 1]])

Ta_b = np.linalg.inv(Tb_a)
pa = Ta_b.dot(pb)
print(pa)
