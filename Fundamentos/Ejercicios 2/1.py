import numpy as np
import rotaciones as r

R = r.rot(90, 'y').dot(r.rot(45, 'z'))


def ejeang(R):

    d1 = (R[1, 0] - R[0, 1])**2
    d2 = (R[2, 0] - R[0, 2])**2
    d3 = (R[2, 1] - R[1, 2])**2
    s = np.sqrt(d1+d2+d3)/2
    print(d3)
    c = (R[0, 0] + R[1, 1] + R[2, 2] - 1)/2
    th = np.arctan2(s, c)

    u = 1.0/(2.*np.sin(th))*np.array([R[2, 1]-R[1, 2], R[0, 2]-R[2, 0], R[1, 0] - R[0, 1]])

    return th, u


th, u = ejeang(R)
print(th)
print(u)


def skew(u):
    su = np.array([[0, -u[2], u[1]],
                   [u[2], 0, -u[0]],
                   [-u[1], u[0], 0]])
    return su


def rodr(th, u):
    s = skew(u)
    Ro = np.eye(3) + s*np.sin(th) + s.dot(s)*(1-np.cos(th))
    return Ro


R1 = rodr(th, u)
print(np.round(R1, 2))
print(np.round(R, 2))
