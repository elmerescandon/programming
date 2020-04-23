import sympy as sp
from sympy.matrices import Matrix

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


# Generacion de variables simbolicas
ph1, ph2, ph3 = sp.symbols("ph1 ph2 ph3")
R = rotz(ph1)*rotx(ph2)*rotz(ph3)


# Parte B
