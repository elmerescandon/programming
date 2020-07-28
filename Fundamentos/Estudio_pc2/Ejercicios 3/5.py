import rotaciones as r
import sympy as sp
from sympy.matrices import Matrix
import numpy as np
from serialrobot import *


def fkine_5(q, l1, l2, l3):
    x = l1*np.cos(q[0]) + l2*np.cos(q[0]+q[1]) + l3*np.cos(q[0]+q[1]+q[2])
    y = l1*np.sin(q[0]) + l2*np.sin(q[0]+q[1]) + l3*np.sin(q[0]+q[1]+q[2])
    p = np.array([x, y])
    return p


num = 70
q1 = np.linspace(-np.pi, np.pi, num)
q2 = np.linspace(-np.pi, np.pi, num)
q3 = np.linspace(-np.pi, np.pi, num)
x = []
y = []

for i in range(num):
    for n in range(num):
        for g in range(num):
            a = np.array([q1[i], q2[n], q3[g]])
            fk = fkine_5(a, 0.5, 0.7, 0.5)
            x.append(fk[0])
            y.append(fk[1])

plt.plot(x, y)
plt.show()
