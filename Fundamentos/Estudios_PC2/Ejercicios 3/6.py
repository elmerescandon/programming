import rotaciones as r
import sympy as sp
from sympy.matrices import Matrix
import numpy as np
from serialrobot import *


def sdh(theta, d, a, alpha):

    T = Matrix([[sp.cos(theta), -sp.cos(alpha)*sp.sin(theta), sp.sin(alpha)*sp.sin(theta), a*sp.cos(theta)],
                [sp.sin(theta),  sp.cos(alpha)*sp.cos(theta), -
                 sp.sin(alpha)*sp.cos(theta), a*sp.sin(theta)],
                [0,                      sp.sin(alpha),            sp.cos(alpha),            d],
                [0,                               0,                     0,            1]])

    return T


q1, q2, q3, d1 = sp.symbols('q1 q2 q3 d1')
sp.init_printing()
T1 = sdh(q1,       0, d1, -sp.pi/2)
T2 = sdh(-sp.pi/2, q2, 0, -sp.pi/2)
T3 = sdh(sp.pi/2, q3, 0, -sp.pi/2)
T = sp.simplify(T1*T2*T3)
T

# Desarrollo  de la cinematica directa


def fkine_6(q):
    nc = np.cos
    ns = np.sin
    d1 = 1
    T = np.array([
        [ns(q[0]),  -nc(q[0]),  0, d1*nc(q[0])-q[1]*ns(q[0])+q[2]*nc(q[0])],
        [-nc(q[0]), -ns(q[0]),  0, d1*ns(q[0])+q[1]*nc(q[0])+q[2]*ns(q[0])],
        [0,                 0, -1,                                       0],
        [0,                 0,  0,                                       1]])

    return np.array([T[0, 3], T[1, 3]])


def ik_newton(xd, q):
    epsilon = 1e-3  # Error mínimo para acabar algoritmo
    max_iter = 10000  # Máximo número de iteraciones
    delta = 1e-9  # Intervalo de derivada numérica
    # Iteraciones: Método de Newton
    for i in range(max_iter):
        q1 = q[0]
        q2 = q[1]
        q3 = q[2]

        # Definir Jacobiano numérico
        JT = (1/delta)*np.array([
            fkine_6([q1+delta, q2, q3]) - fkine_6([q1, q2, q3]),
            fkine_6([q1, q2+delta, q3]) - fkine_6([q1, q2, q3]),
            fkine_6([q1, q2, q3+delta]) - fkine_6([q1, q2, q3])])
        J = JT.T
        fk = fkine_6(q)
        e = xd - fk
        q = q + np.dot(np.linalg.pinv(J), e)
        if(np.linalg.norm(e) < epsilon):
            break
        if(i == max_iter-1):
            print("En Newton. Cambiar epsilon o aumentar iteraciones, error = {}".format(e))
    return q


def ik_gradient(xd, q):
    epsilon = 1e-3  # Error mínimo para acabar algoritmo
    max_iter = 1000  # Máximo número de iteraciones
    delta = 1e-9  # Intervalo de derivada numérica
    # Iteraciones: Método de Newton
    alpha = 0.08
    for i in range(max_iter):
        q1 = q[0]
        q2 = q[1]
        q3 = q[2]

        # Definir Jacobiano numérico
        JT = (1/delta)*np.array([
            fkine_6([q1+delta, q2, q3]) - fkine_6([q1, q2, q3]),
            fkine_6([q1, q2+delta, q3]) - fkine_6([q1, q2, q3]),
            fkine_6([q1, q2, q3+delta]) - fkine_6([q1, q2, q3])])
        J = JT.T
        fk = fkine_6(q)
        e = xd - fk
        q = q + alpha*JT.dot(e)
        if(np.linalg.norm(e) < epsilon):
            break
        if(i == max_iter-1):
            print("En gradiente. Cambiar alpha o aumentar iteraciones, error = {}".format(e))
    return q


# Cinemática Inversa
xd = np.array([[0, 2],
               [-1, 3],
               [5, 1],
               [-6, -4]])  # Matriz de Valores deseados en el espacio cartesiano
qi = np.array([0, 0, 0])  # Valor inicial en el espacio articular
qo_newton = []  # Valores obtenidos con Método Numérico de Newton
qo_gradient = []  # Valores obtenidos con Método Numérico de Descenso de Gradiente
xo_newton = []
xo_gradient = []


for i in range(len(xd)):
    a = ik_newton(xd[i, :], qi)
    b = ik_gradient(xd[i, :], qi)
    c = fkine_6(a)
    d = fkine_6(b)
    xo_newton.append([c[0], c[1]])
    xo_gradient.append([d[0], d[1]])
    qo_gradient.append(b)
    qo_newton.append(b)

print("Los valores reales de posiciones deseadas son: {}".format(xd))
print("Los valores obtenidos por Newton son: {}".format(np.round(xo_newton, 2)))
print("Los valores obtenidos por Gradiente son: {}".format(np.round(xo_gradient, 2)))
# print("Los valores de las articulaciones según la cinemática inversa es:{}".format(np.round(q, 3)))
# pd = np.round(fkine_6(q))
# print("Los valores usados con la cinemática indirecta de comprobación{}".format(pd))

# Workspace
num = 70
q1 = np.linspace(-np.pi, np.pi, num)
q2 = np.linspace(-3, 3, num)
q3 = np.linspace(-4, 4, num)
x = []
y = []

for i in range(num):
    for n in range(num):
        for g in range(num):
            a = np.array([q1[i], q2[n], q3[g]])
            fk = fkine_6(a)
            x.append(fk[0])
            y.append(fk[1])

plt.plot(x, y)
plt.show()
