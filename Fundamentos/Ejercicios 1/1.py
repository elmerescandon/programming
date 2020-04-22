import sympy as sp
from sympy.matrices import Matrix

cos = sp.cos
sin = sp.sin

# Definir las matrices con de rotacion de Y y Z con simbolicos


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


sp.init_printing()
# Generacion de variables simbolicas
t, p = sp.symbols("t p")
# Rotacion deseada
R = rotz(t)*roty(p)
print(R)
