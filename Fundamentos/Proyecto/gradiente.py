import numpy as np
import sympy as sp


def sTrasl(x, y, z):
    """ Matriz de transformada homogenea de traslacion
    """
    T = sp.Matrix([[1,0,0,x],
                    [0,1,0,y],
                    [0,0,1,z],
                    [0,0,0,1]])
    return T

def sTrotx(ang):
    """ Matriz de transformada homogenea alrededor de X
    """
    Tx = sp.Matrix([[1, 0,0,0],
                    [0, sp.cos(ang),-sp.sin(ang),0],
                    [0, sp.sin(ang), sp.cos(ang),0],
                    [0, 0, 0, 1]])
    return Tx

def sTroty(ang):
    """ Matriz de transformada homogenea alrededor de Ya
    """
    Ty = sp.Matrix([[sp.cos(ang),0,sp.sin(ang),0],
                    [0,1,0,0],
                    [-sp.sin(ang),0,sp.cos(ang),0],
                    [0,0,0,1]])
    return Ty

def sTrotz(ang):
    """ Matriz de transformada homogenea alrededor de Z
    """
    Tz = sp.Matrix([[sp.cos(ang),-sp.sin(ang),0,0],
                    [sp.sin(ang), sp.cos(ang),0,0],
                    [0,0,1,0],
                    [0,0,0,1]])
    return Tz
def sTdh(d, th, a, alpha):
    """ Matriz de transformación homogénea de Denavit-Hartenberg
    """
    cth = sp.cos(th); sth = sp.sin(th)
    ca = sp.cos(alpha); sa = sp.sin(alpha)
    Tdh = sp.Matrix([[cth, -ca*sth,  sa*sth, a*cth],
                     [sth,  ca*cth, -sa*cth, a*sth],
                     [0,        sa,     ca,      d],
                     [0,         0,      0,      1]])
    return Tdh

def jacob_1(q11,q12,q13):
    cos = np.cos
    sin = np.sin
    J1_np = np.array([[0, -105*cos(q12) - 120*cos(q12 + q13), -120*cos(q12 + q13)],
                      [-25*sin(q11) + 105*cos(q11)*cos(q12) + 120*cos(q11)*cos(q12 + q13), -105*sin(q11)*sin(q12) - 120*sin(q11)*sin(q12 + q13), -120*sin(q11)*sin(q12 + q13)],
                      [105*sin(q11)*cos(q12) + 120*sin(q11)*cos(q12 + q13) + 25*cos(q11), 105*sin(q12)*cos(q11) + 120*sin(q12 + q13)*cos(q11), 120*sin(q12 + q13)*cos(q11)]])
    return  J1_np

def fk_1(q11,q12,q13):
    cos = np.cos
    sin = np.sin
    F1_np = np.array([[-105*sin(q12) - 120*sin(q12 + q13) + 125],
                      [105*sin(q11)*cos(q12) + 120*sin(q11)*cos(q12 + q13) + 25*cos(q11) + 75],
                      [25*sin(q11) - 105*cos(q11)*cos(q12) - 120*cos(q11)*cos(q12 + q13)]])
    return np.array([F1_np[0,0],F1_np[1,0],F1_np[2,0]])
