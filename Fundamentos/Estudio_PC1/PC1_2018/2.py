import numpy as np
import rotaciones as r


# Obtener el sistema 1 con respecto a 2

a = 0.5
c = 0.375
b = c
th = np.arctan2(0.5, 0.375)
th2 = 90 - th
RT1 = r.rot(-90, 'x').dot(r.rot(53, 'z'))
TT1 = np.array([[RT1[0, 0], RT1[0, 1], RT1[0, 2], a],
                [RT1[1, 0], RT1[1, 1], RT1[1, 2], 0],
                [RT1[2, 0], RT1[2, 1], RT1[2, 2], c],
                [0, 0, 0, 1]])

RT2 = r.rot(90, 'x').dot(r.rot(216.86, 'z'))
TT2 = np.array([[RT2[0, 0], RT2[0, 1], RT2[0, 2], a],
                [RT2[1, 0], RT2[1, 1], RT2[1, 2], b],
                [RT2[2, 0], RT2[2, 1], RT2[2, 2], c],
                [0, 0, 0, 1]])

print(np.round(TT1, 2))
print(np.round(TT2, 2))
