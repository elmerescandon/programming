import rotaciones as r
import numpy as np
from serialrobot import *
cos = np.cos
sin = np.sin
pi = np.pi


def dh(theta, d, a, alpha):

    T = np.array([[cos(theta), -cos(alpha)*sin(theta), sin(alpha)*sin(theta), a*cos(theta)],
                  [sin(theta),  cos(alpha)*cos(theta), -sin(alpha)*cos(theta), a*sin(theta)],
                  [0,                      sin(alpha),            cos(alpha),            d],
                  [0,                               0,                     0,            1]])

    return T


def direct_scara(q):
    l1 = 1
    l2 = 1
    l3 = 1
    l4 = 0.5
    T1 = dh(pi+q[0], l1, l2, 0)
    T2 = dh(-pi/2+q[1], 0, l3, 0)
    T3 = dh(0, -l4+q[2], 0, 0)
    T4 = dh(pi/2+q[3], 0, 0, pi)
    T = T1.dot(T2).dot(T3).dot(T4)
    return T


r2d = np.rad2deg
q = np.array([r2d(0), r2d(0), 0, r2d(0)])
T = np.round(direct_scara(q), 2)
print("El robot SCARA  con los ángulos q1={},q2={},q3={},q4={}".format(q[0], q[1], q[2], q[3]))
print(T)

l1 = 1
l2 = 1
l3 = 1
l4 = 0.5
L = [[l1, pi, l2, 0, 'r'],
     [0, -pi/2, l3, 0, 'r'],
     [-l4, 0, 0, 0, 'p'],
     [0, pi/2, 0, pi, 'r']]
scara = SerialRobot(L, name='scara')
T = scara.fkine([0, 0, 0, 0], verbose=False)
print(np.round(T, 3))

alims = [[-2, 2], [-2, 2], [-0.2, 1.3]]
scara.plot([0, 0, 0, 0], axlimits=alims)
