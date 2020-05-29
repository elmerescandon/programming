import sympy as sp
from sympy.matrices import Matrix
import numpy as np
import rotaciones as r
import matplotlib.pyplot as plt

q1, q2 = sp.symbols(r'q_1 q_2')
l1 = 1
l2 = 1
x = l1*sp.cos(q1) + l2*sp.cos(q1+q2)
y = l1*sp.sin(q1) + l2*sp.sin(q1+q2)
theta = q1+q2

fk = Matrix([[x],
             [y],
             [theta]])
q = Matrix([q1, q2])

J = fk.jacobian(q)
J


def fk_rr(q):
    l1 = 1
    l2 = 1
    x = l1*np.cos(q[0]) + l2*np.cos(q[0]+q[1])
    y = l1*np.sin(q[0]) + l2*np.sin(q[0]+q[1])
    return np.array([x, y])


def jacobian_rr(q):
    J = np.array([[-np.sin(q[0])-np.sin(q[0]+q[1]), -np.sin(q[0]+q[1])],
                  [np.cos(q[0])+np.cos(q[0]+q[1]), np.cos(q[0]+q[1])]])
    return J


q = np.array([0.5, 0.5])
xd = np.array([1.2, 1.5])

dt = 0.005
k = 1
t = np.linspace(0, 15, num=int(15/dt))
epsilon = 1e-3
e_array = np.zeros((len(t), 2))
for i in range(len(t)):
    x = fk_rr(q)
    J = jacobian_rr(q)
    e = x - xd
    if (np.linalg.norm(e) < epsilon):
        break
    e_dot = -k*e
    q_dot = np.linalg.pinv(J).dot(e_dot)
    q = q + dt*q_dot
    e_array[i, 0] = e[0]
    e_array[i, 1] = e[1]


plt.subplot(121)
plt.plot(t[0:len(e_array)], e_array[:, 0])
plt.title('Error en X')
plt.grid()
plt.xlabel("tiempo [s]")
plt.ylabel("y [m]")
plt.tight_layout(pad=3.0)
plt.subplot(122)
plt.plot(t[0:len(e_array)], e_array[:, 1])
plt.title('Error en Y')
plt.grid()
plt.xlabel("tiempo [s]")
plt.ylabel("y [m]")
plt.tight_layout(pad=3.0)
plt.show()
