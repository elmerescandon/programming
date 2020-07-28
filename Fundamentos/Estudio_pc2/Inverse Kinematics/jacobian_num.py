import numpy as np
import matplotlib.pyplot as plt
import rotaciones as r


def fkine(q):
    x = np.cos(q[0]) + np.cos(q[0]+q[1])
    y = np.sin(q[0]) + np.sin(q[0]+q[1])
    return np.array([x, y])


q1 = 0.5
q2 = 1.0
delta = 0.001
JT = 1/delta*np.array([
    fkine([q1+delta, q2]) - fkine([q1, q2]),
    fkine([q1, q2+delta]) - fkine([q1, q2])])
J = JT.transpose()
print(J)
