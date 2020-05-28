import numpy as np
import rotaciones as r
import sympy as sp
import matplotlib.pyplot as plt

# Robot R-R - Calculo Simbólico
sp.init_printing()
q1, q2, l1, l2 = sp.symbols('q1 q2 l1 l2')
T_01 = r.strotz(q1)*r.strasl(l1, 0, 0)
T_12 = r.strotz(q2)*r.strasl(l2, 0, 0)
T_0e = T_01*T_12
# sp.pprint(sp.simplify(T_0e))

# Robot R-R - Calculo Numerico


def direct_kinematics_rr(q, l1, l2):

    T_01 = r.trot(q[0], 'z').dot(r.trasl(l1, 0, 0))
    T_1e = r.trot(q[1], 'z').dot(r.trasl(l2, 0, 0))
    T_0e = T_01.dot(T_1e)
    return T_01, T_0e


# Gráfica del robot dada una configuración articular
def graph_robot2d(q, l1, l2, show_axis=True, k=0.5):
    """ Grafica el robot según la configuración articular
    """
    T1, Te = direct_kinematics_rr(q, l1, l2)
    plt.clf()
    # Cuerpo del robot
    plt.plot([0, T1[0, 3]], [0, T1[1, 3]], linewidth=3, color='b')
    plt.plot([T1[0, 3], Te[0, 3]], [T1[1, 3], Te[1, 3]], linewidth=3, color='b')
    # Puntos en las articulaciones
    plt.plot(0, 0, color='r', marker='o', markersize=8)
    plt.plot(T1[0, 3], T1[1, 3], color='r', marker='o', markersize=8)
    # Efector final (definido por 4 puntos)
    p1 = np.array([0, 0.1, 0, 1])
    p2 = np.array([0.2, 0.1, 0, 1])
    p3 = np.array([0, -0.1, 0, 1])
    p4 = np.array([0.2, -0.1, 0, 1])
    p1 = Te.dot(p1)
    p2 = Te.dot(p2)
    p3 = Te.dot(p3)
    p4 = Te.dot(p4)
    # Gráfico del efector final
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='b', linewidth=3)
    plt.plot([p3[0], p4[0]], [p3[1], p4[1]], color='b', linewidth=3)

    plt.plot([p1[0], p3[0]], [p1[1], p3[1]], color='b', linewidth=3)
    # Sistema de referencia del efector final y de la base
    if (show_axis):
        plt.plot([Te[0, 3], Te[0, 3]+k*Te[0, 0]], [Te[1, 3], Te[1, 3]+k*Te[1, 0]], color='r')
        plt.plot([Te[0, 3], Te[0, 3]+k*Te[0, 1]], [Te[1, 3], Te[1, 3]+k*Te[1, 1]], color='g')
        plt.plot([0, k], [0, 0], color='r')
        plt.plot([0, 0], [0, k], color='g')
    # Plot
    plt.axis('equal')
    plt.grid('on')


l1 = 1.0
l2 = 1.0
# q = [np.deg2rad(30), np.deg2rad(40)]
# graph_robot2d(q, l1, l2, show_axis=True)
plt.show()
for a in range(30):
    q = np.array([30+a, 40+0.5*a])
    graph_robot2d(np.deg2rad(q), l1, l2)
    plt.pause(0.0001)
plt.show()
