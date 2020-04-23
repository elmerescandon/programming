import numpy as np

cos = np.cos
sin = np.sin
pi = np.pi


def rot(th, a):
    """
    Genera una matriz de Rotación alrededor de cualquier
    eje independiente usando los 9 parámetros para la matriz de rotación
    Entradas: th -> sexagesimales
              a -> eje de rotacion deseado
    """
    th = np.deg2rad(th)
    if (a == 'x'):
        R = np.array([[1,       0,        0],
                      [0, cos(th), -sin(th)],
                      [0, sin(th),  cos(th)]])
    elif (a == 'y'):
        R = np.array([[cos(th),      0, sin(th)],
                      [0,      1,      0],
                      [-sin(th),     0, cos(th)]])
    elif (a == 'z'):
        R = np.array([[cos(th), -sin(th), 0],
                      [sin(th), cos(th), 0],
                      [0,      0,    1]])
    return R


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


def skew(u):
    su = np.array([[0, -u[2], u[1]],
                   [u[2], 0, -u[0]],
                   [-u[1], u[0], 0]])
    return su


def rodr(th, u):
    s = skew(u)
    Ro = np.eye(3) + s*np.sin(th) + s.dot(s)*(1-np.cos(th))
    return Ro
