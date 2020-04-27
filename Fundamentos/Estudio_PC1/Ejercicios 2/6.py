import numpy as np
import rotaciones as r


R1 = np.array([[-0.5, 0, -np.sqrt(3)/2],
               [0, 1, 0],
               [-np.sqrt(3)/2, 0, -0.5]])

R2 = np.array([[-0.5, 0, -np.sqrt(3)/2],
               [0, 1,             0],
               [np.sqrt(3)/2, 0,          -0.5]])

R3 = np.array([[-0.5, 0, -np.sqrt(3)/2],
               [0, 1, 0],
               [np.sqrt(3)/2, 0, -0.5]])

# Pregunta 1
# print(r.matriz_so3(R1))
# print(r.matriz_so3(R2))  # Valida
# print(r.matriz_so3(R3))  # Valida

# Pregunta 2
q1 = r.quaterion(R2)
q2 = r.quaterion(R3)

RR1 = r.rquater(q1)
RR2 = r.rquater(q2)
print(R3)
# print(RR1)
print(RR2)

# Pregunta 3

ejeang1 = r.ejeang(R2)
ejeang2 = r.ejeang(R3)

print(ejeang1)
print(ejeang2)
