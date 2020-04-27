import numpy as np
import rotaciones as r


def rod_vect(p, u, th):
    u1 = np.sqrt(u[1, 0]**2 + u[0, 0]**2 + u[2, 0]**2)
    u = u/u1
    temp = r.cruz(u, p)
    pb = p*np.cos(th) + temp*np.sin(th) + u*(u.T.dot(p))*(1-np.cos(th))
    return pb


p = np.array([[3],
              [1],
              [1]])
u = np.array([[2],
              [1],
              [2]])
th = np.deg2rad(30)
pb = rod_vect(p, u, th)
print(np.round(pb, 2))

R = r.rodr(th, u)
print(np.round(R, 3))
pb2 = R.dot(p)
print(pb2)
