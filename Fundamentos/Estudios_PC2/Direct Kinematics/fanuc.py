import rotaciones as r
import numpy as np
from serialrobot import *
cos = np.cos
sin = np.sin
pi = np.pi
d2r = np.deg2rad


def dh(theta, d, a, alpha):

    T = np.array([[cos(theta), -cos(alpha)*sin(theta), sin(alpha)*sin(theta), a*cos(theta)],
                  [sin(theta),  cos(alpha)*cos(theta), -sin(alpha)*cos(theta), a*sin(theta)],
                  [0,                      sin(alpha),            cos(alpha),            d],
                  [0,                               0,                     0,            1]])

    return T


def direct_fanuc(q):

    T1 = dh(pi+q[0],    450,  -150,  pi/2)
    T2 = dh(pi/2+q[1],    0,   600,     0)
    T3 = dh(pi+q[2],      0,  -200,  pi/2)
    T4 = dh(pi+q[3],    640,     0,  pi/2)
    T5 = dh(pi+q[4],      0,     0,  pi/2)
    T6 = dh(q[5],         0,     0,     0)
    T = T1.dot(T2).dot(T3).dot(T4).dot(T5).dot(T6)
    return T


q = d2r(np.array([0, 0, 0, 0, 0, 0]))
T = np.round(direct_fanuc(q), 3)

print("El robot FANUC  con los ángulos q1={},q2={},q3={},q4={},q5={},q6={}".format(
    q[0], q[1], q[2], q[3], q[4], q[5]))
print(T)4


L = [[0.450, pi,   -0.150,  pi/2, 'r'],
     [0,  pi/2,       0.600,     0, 'r'],
     [0, pi,    -0.200,  pi/2, 'r'],
     [0.640, pi,      0,  pi/2, 'r'],
     [0, pi,    0,  pi/2, 'r'],
     [0, 0,      0,     0, 'r']]
fanuc = SerialRobot(L, name='fanuc')
alims = [[-0.1, 1.3], [-0.7, 0.7], [-0.1, 1.4]]
fanuc.plot([0, 0.5, -0.5, 0., -0, 0], axlimits=alims, ascale=0.3, ee=False)
