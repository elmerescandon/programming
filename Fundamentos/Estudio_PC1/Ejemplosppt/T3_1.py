import numpy as np
import rotaciones as r

# Tema 3 - Slide 29 (2020-1)
R1 = np.array([[-1/2,          0, -np.sqrt(3)/2],
               [0,             1,             0],
               [-np.sqrt(3)/2, 0,          -1/2]])
R2 = np.array([[-1/2,          0, -np.sqrt(3)/2],
               [0,             1,             0],
               [np.sqrt(3)/2, 0,          -1/2]])

print(r.matriz_so3(R1))
print(r.matriz_so3(R2))
