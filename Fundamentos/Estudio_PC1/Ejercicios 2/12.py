import numpy as np
import rotaciones as r

# Obtener el sistema 1 con respecto a 2
R12 = r.rot(180, 'z').dot(r.rot(53, 'x'))

T12 = np.array([[R12[0, 0], R12[0, 1], R12[0, 2], 4],
                [R12[1, 0], R12[1, 1], R12[1, 2], 3],
                [R12[2, 0], R12[2, 1], R12[2, 2], -4],
                [0, 0, 0, 1]])

T21 = np.linalg.inv(T12)

# Obtener el sistema 3 con respecto a 0
R03 = r.rot(-90, 'y').dot(r.rot(-143, 'x'))
T03 = np.array([[R03[0, 0], R03[0, 1], R03[0, 2], 0],
                [R03[1, 0], R03[1, 1], R03[1, 2], 4],
                [R03[2, 0], R03[2, 1], R03[2, 2], 0],
                [0, 0, 0, 1]])
# Obtener el sistema 1 con respecto a 0
R01 = r.rot(-90, 'y').dot(r.rot(90, 'x'))
T01 = np.array([[R01[0, 0], R01[0, 1], R01[0, 2], 3],
                [R01[1, 0], R01[1, 1], R01[1, 2], 0],
                [R01[2, 0], R01[2, 1], R01[2, 2], 0],
                [0, 0, 0, 1]])

T23 = T21.dot(np.linalg.inv(T01)).dot(T03)
print(np.round(T23, 2))
