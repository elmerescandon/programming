# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np
from helper import leer_landmarks, leer_sensor_odom, plot_robot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#%matplotlib qt
fig = plt.figure()
plt.axis([-1, 12, 0, 10])
# plt.ion(): #plt.show()


def prediccion_ekf(odom, X, P):
    """
    Estimación del estado del robot (X) y su matriz de covarianza (P) según
    el modelo de movimiento

    X: vector 3x1 que representa (x,y,theta) del robot
    P: matriz 3x3 que representa la covarianza

    """

    # Estado del robot
    x = X[0]; y = X[1]; theta = X[2]
    # Valores delta del modelo
    delta_rot1 = odom['r1']
    delta_trans = odom['t']
    delta_rot2 = odom['r2']

    """
    Completar la implementación debajo de este comentario
    """

    # Ruido del movimiento: R (completar)

    R = np.array([[0.2, 0, 0],
                  [0, 0.2, 0],
                  [0,0,0.2]])
    # Movimiento sin ruido (completar)
    """
    El modelo de movimiento del robot según la odometría
    tiene entrada u, donde se representa porque la secuencia
    de giro (delta_rot1), desplazamiento(delta_trans) y
    giro (delta_rot2).
    """
    x = x + delta_trans*np.cos(theta+delta_rot1)
    y = y + delta_trans*np.sin(theta+delta_rot1)
    theta = theta + delta_rot1 + delta_rot2
    X = np.array([x,y,theta])
    # Jacobiano con respecto al estado (completar)
    Jacob = np.array([[1,0,-delta_trans*np.sin(theta+delta_rot1)],
                      [0,1,delta_trans*np.cos(theta + delta_rot1)],
                      [0,0,1]])

    # Jacobiano de la matriz de estado con respecto al error
    Fe = np.array([[1,0,0],
                   [0,1,0],
                   [0,0,1]])
    P = Jacob.dot(P).dot(Jacob.T) + Fe.dot(R).dot(Fe.T)
    return X, P


def correccion_ekf(sensor, X, P, landmarks):
    """
    Actualización de la estimación usando el modelo del sensor (con solo
    mediciones de rango)

    X: vector 3x1 que representa (x,y,theta) del robot
    P: matrix 3x3 que representa la covarianza

    """

    # Estado del robot
    x = X[0]; y = X[1];
    # Landmarks medidos (ids) y sus rangos
    ids = sensor['id']
    rangos = sensor['rango']

    """
    Completar la implementación debajo de este comentario
    """

    # Mediciones de rango para cada landmark (función h)
    H = []; Z = []; h = []
    for i in range(len(ids)):
        # Medición
        Z.append(rangos[i])
        # Obtención de coordenadas x, y para cada landmark observado
        # (en el sistema inercial)
        lm_id = ids[i]
        lx = landmarks[lm_id][0]
        ly = landmarks[lm_id][1]

        # Calcular la medición esperada de rango para cada landmark (lx, ly)
        # *** Completar h_i ***
        """
        Función h que obtiene el rango estimado a partir de la predicción del estado
        y la posición real dee los landmarks.
        """
        q = (lx-x)**2 + (ly-y)**2
        h_i = np.sqrt(q)

        # Calcular cada fila de la matriz H (derivada de h_i con respecto al
        # estado), para cada medición de landmark (lx, ly)
        # H_i: vector de 1x3
        # *** Completar H_i ***
        """
        La Matriz H es el jacobiano de la función h con respecto al estado.
        """
        H_i = (1/q)*np.array([-h_i*(lx-x),-h_i*(ly-y),0])

        # Incrementar los elementos (filas) de la matriz H y las mediciones
        H.append(H_i); h.append(h_i)

    # Covarianza de las mediciones (completar)
    "Conversión de la matrices H y h a numpy / Inicializar matriz de covarianza"
    Q = 0.5*np.eye(len(H))
    H = np.array(H)
    h = np.array(h)
    # Ganancia de Kalman (completar)
    temp = Q + H.dot(P).dot(H.T)
    K = P.dot(H.T).dot(np.linalg.inv(temp))

    # Corrección de la media y la covarianza (completar)
    X = X + K.dot(Z-h)
    P = (np.eye(len(K)) - K.dot(H)).dot(P)


    return X, P

# =======================================================================
#
# Filtro de Kalman Extendido para la estimación de posición/orientación
#
# =======================================================================

print("Leyendo posiciones de landmarks")
landmarks = leer_landmarks("data_landmarks.dat")

print("Leyendo datos del sensor")
sensor = leer_sensor_odom("data_sensor.dat")

# Estado inicial
X = [0.0, 0.0, 0.0]
# Matriz de covarianza inicial
P = np.array([[1.0, 0.0, 0.0],
              [0.0, 1.0, 0.0],
              [0.0, 0.0, 1.0]])
# Límites del mapa
map_limits = [-1, 12, -1, 10]

# t es el "tiempo"
#for t in range(10):
for t in range(int(len(sensor)/2)):
    # Gráfico del estado actual
    plot_robot(X, P, landmarks, map_limits)
    # Predicción con EKF
    X, P = prediccion_ekf(sensor[t,'odom'], X, P)
    print(X)
    # Corrección con EKF
    X, P = correccion_ekf(sensor[t, 'sensor'], X, P, landmarks)
plt.show('hold')
