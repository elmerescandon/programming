import numpy as np
import rotaciones as r

# Tema 3 - Slide 30 (2020-1)
R2 = np.array([[0.25,         0.866,         0.433],
               [0.433,          -0.5,          0.75],
               [0.866,             0,          -0.5]])

print(np.round(np.linalg.inv(R2), 4))
print(r.matriz_so3(R2))
print(R2.T)
