import numpy as np


def Tdh(d, th, a, alpha):
    cth = np.cos(np.deg2rad(th))
    sth = np.sin(np.deg2rad(th))
    ca = np.cos(np.deg2rad(alpha))
    sa = np.sin(np.deg2rad(alpha))
    Tdh = np.array([[cth, -ca*sth,  sa*sth, a*cth],
                    [sth,  ca*cth, -sa*cth, a*sth],
                    [0,        sa,     ca,      d],
                    [0,         0,      0,      1]])
    return Tdh


def cdirecta_pata(q1, q2, q3, d1, d2, a2, a3):
    Tdh_1 = Tdh(180+q1, d1, 90, 0)
    Tdh_2 = Tdh(180+q2, d2, 0, a2)
    Tdh_3 = Tdh(q3, 0, 0, a3)
    Tf = Tdh_1.dot(Tdh_2).dot(Tdh_3)
    return Tf


q1 = 0
q2 = 0
q3 = 0
d1 = 3
d2 = 0.5
a2 = 5
a3 = 5
