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


q1, q2, l = sp.symbols('q1 q2 l')
sp.init_printing()
T1 = sdh(q1+sp.pi, 0, -l, sp.pi/2)
T2 = sdh(0, q2, 0, 0)
T = sp.simplify(T1*T2)

# Resolución de cinemática directa


def fkine_4(q):
    l = 0.5
    p = np.array([l*np.cos(q[0]) - q[1]*np.sin(q[0]),
                  l*np.sin(q[0]) + q[1]*np.cos(q[0])])
    return p


def ikine_r(p):
    l = 2
    q2 = np.sqrt(p[0]**2 + p[1]**2 - l**2)
    if (np.arctan2(p[1], p[0]) < 0):
        q2 = -q2

    cq1 = (p[0]*l + p[1]*q2)/(l**2 + q2**2)
    sq1 = (-1/q2)*(p[0] - l*cq1)
    q1 = np.arctan2(sq1, cq1)
    q = np.array([q1, q2])
    return q


q1 = np.array([np.pi/6, 1])
a = fkine_4(q1)
b = ikine_r(a)
# print(q1)
# print(b)

num = 1000
q1 = np.linspace(-np.pi/2, np.pi/2, num)
q2 = np.linspace(-4, 4, num)
x = []
y = []

for i in range(num):
    for n in range(num):
        a = np.array([q1[i], q2[n]])
        fk = fkine_4(a)
        x.append(fk[0])
        y.append(fk[1])

plt.plot(x, y)
plt.show()
