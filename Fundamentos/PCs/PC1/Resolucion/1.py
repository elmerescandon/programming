import sympy as sp
from sympy.matrices import Matrix
import numpy as np
import rotaciones as r
cos = sp.cos
sin = sp.sin

# Definir las matrices con de rotacion de Y y Z con simbolicos
sp.init_printing()


def roty(ang):

    Ry = Matrix([[cos(ang), 0, sin(ang)],
                 [0, 1,        0],
                 [-sin(ang), 0, cos(ang)]])
    return Ry


def rotz(ang):
    Rz = Matrix([[cos(ang), -sin(ang), 0],
                 [sin(ang),  cos(ang), 0],
                 [0, 0, 1]])
    return Rz


def rotx(ang):
    Rx = Matrix([[1,       0,        0],
                 [0, cos(ang), -sin(ang)],
                 [0, sin(ang),  cos(ang)]])
    return Rx


ph1, ph2, ph3 = sp.symbols("ph1 ph2 ph3")
Rs = rotz(ph1)*rotx(ph2)*roty(ph3)
print(Rs)

R = np.array([[0.949, -0.158, -0.273],
              [-0.235, 0.226, -0.946],
              [0.211, 0.961, 0.177]])
th2 = np.arctan2(R[2, 1], np.sqrt(R[1, 1]**2+R[0, 1]**2))
th1 = np.arctan2(-R[0, 1]/np.cos(th2), R[1, 1]/np.cos(th2))
th3 = np.arctan2(-R[2, 0]/np.cos(th2), R[2, 2]/np.cos(th2))

th1d = np.rad2deg(th1)
th2d = np.rad2deg(th2)
th3d = np.rad2deg(th3)
print(th1d, th2d, th3d)

# Parte 2
Rsp = Rs.subs([(ph2, (sp.pi/2))])
R2 = np.array([[-0.906, 0, -0.423],
               [0.423, 0, 0.906],
               [0, 1, 0]])
print(Rsp)
ang1 = np.arctan2(0.423, -0.906)
ang1d = np.rad2deg(ang1)
print(ang1d)
