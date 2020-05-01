import numpy as np
import rotaciones as r

q = np.array([[0.94], [0], [0], [0.34]])
RIR = r.rquater(q)


# Matriz de trasnformacin del sistema inercial con respecto al robot
RRI = RIR.T
TRI = np.array([[RRI[0, 0], RRI[0, 1], RRI[0, 2], -5],
                [RRI[1, 0], RRI[1, 1], RRI[1, 2], 2],
                [RRI[2, 0], RRI[2, 1], RRI[2, 2], -0.2],
                [0, 0, 0, 1]])

# Se obtiene la matriz de rotacion del sistema inercial con respecto
# al robot
TIR = np.linalg.inv(TRI)

# Una vez se obtiene la matriz del robot con respecto al sistema inercial,
# se puede multiplicar por los puntos obtenidos en el inciso (A) segun
# se observa en las imagenes adjuntas del archivo PDF
p_caso1 = np.array([[2.16], [-0.1], [0.3], [1]])
p_caso2 = np.array([[2.12], [0.789], [-1.099], [1]])
p_caso3 = np.array([[1.998], [-1.795], [-1.9438], [1]])


p1_inercial = TIR.dot(p_caso1)
p2_inercial = TIR.dot(p_caso2)
p3_inercial = TIR.dot(p_caso3)

print("P1: ", p1_inercial)
print("P2: ", p2_inercial)
print("P3: ", p3_inercial)
