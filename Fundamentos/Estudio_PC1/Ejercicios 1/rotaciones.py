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
