import numpy as np
import rotaciones as r

# Verificar que sea una matriz de rotacion,
# se usa la funcion matriz so3 que retorna un
# booleano indicando si es o no una matriz SO3


M1 = np.array([[0.8291,        -0.4466,        0.3363],
               [0.5069,         0.8542,       -0.1153],
               [-0.2358,        0.2661,        0.9347]])

M2 = np.array([[-0.9151,        -0.4466,        0.3363],
               [0.4020,         0.8542,       -0.1153],
               [0.0298,        0.2661,        0.9347]])

R1 = np.array([[1,        0,        0],
               [0,         0.5,       -0.866],
               [0,        0.866,        0.5]])

R2 = np.array([[0,        0,        1],
               [0,         -1,       0],
               [1,        0,        0]])


# print(R1.dot(R2))
#print(np.rad2deg(np.arctan2(-0.866, -0.5)))

print(np.round(r.rot(-90, 'y').dot(r.rot(90, 'x'))), 2)
