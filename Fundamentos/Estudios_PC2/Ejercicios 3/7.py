import rotaciones as r
import sympy as sp
from sympy.matrices import Matrix
import numpy as np
from serialrobot import *


def sdh(d, theta, a, alpha):

    T = Matrix([[sp.cos(theta), -sp.cos(alpha)*sp.sin(theta), sp.sin(alpha)*sp.sin(theta), a*sp.cos(theta)],
                [sp.sin(theta),  sp.cos(alpha)*sp.cos(theta), -
                 sp.sin(alpha)*sp.cos(theta), a*sp.sin(theta)],
                [0,                      sp.sin(alpha),            sp.cos(alpha),            d],
                [0,                               0,                     0,            1]])

    return T


q1, q2 = sp.symbols('q1 q2 ')
sp.init_printing()
a1 = 0.2
T1 = sdh(0,     q1, a1, -sp.pi/2)
T2 = sdh(q2, sp.pi,  0,  sp.pi/2)
T = sp.simplify(T1*T2)
T
fkine_s = Matrix([[T[0, 3]],
                  [T[1, 3]]])
fkine_s
q_s = Matrix([q1, q2])
fkine_s
J_7 = fkine_s.jacobian(q_s)
J_7


def fkine_7(q):

    fk = np.array([-q[1]*np.sin(q[0]) + 0.2*np.cos(q[0]),
                   q[1]*np.cos(q[0]) + 0.2*np.sin(q[0])])
    return fk


def jacob(q):
    J = np.array([
        [-q[1]*np.cos(q[0]) - 0.2*np.sin(q[0]), -np.sin(q[0])],
        [-q[1]*np.sin(q[0]) + 0.2*np.cos(q[0]), np.cos(q[0])]])
    return J


xd = np.array([-2, -3])
qk = np.array([-1, 2])
qk_1 = np.array([-2.7742, -0.6519])
e = xd - fkine_7(qk)
q_diff = qk_1 - qk
q_diff = np.array([[q_diff[0]],
                   [q_diff[1]]])
e = np.array([[e[0]],
              [e[1]]])
J_real = jacob(qk)


f = (J_real.T).dot(e)
# print(q_diff)
# print(f)
# print(q_diff/f)

# Se encuentra entonces que es el método de Gradiente, con un alfa de 0.5


def ik_gradient(xd, q):
    epsilon = 1e-3  # Error mínimo para acabar algoritmo
    max_iter = 100  # Máximo número de iteraciones
    # Iteraciones: Método de Newton
    #alpha = 0.5
    alpha = 0.1
    for i in range(max_iter):
        q1 = q[0]
        q2 = q[1]
        # Definir Jacobiano numérico
        J = jacob(q)
        fk = fkine_7(q)
        e = xd - fk
        q = q + alpha*(J.T).dot(e)
        if(np.linalg.norm(e) < epsilon):
            print("Sin problemas, con error de {}".format(e))
            break
        if(i == max_iter-1):
            print("En gradiente. Cambiar alpha o aumentar iteraciones, error = {}".format(e))
    return q


# (b) Se debe reducir el alpha para obtener lso valores adecuados de  q deseado
q_des = ik_gradient(xd, qk)
print(q_des)
# El q deseado es [-3.67408253  3.59914654]


# (C) hallar el
