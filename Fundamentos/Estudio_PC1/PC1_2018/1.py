import sympy as sp
from sympy.matrices import Matrix

cos = sp.cos
sin = sp.sin


# Generacion de variables simbolicas
A, B, C, D, E, F = sp.symbols("A B C D E F")
R = Matrix([[0, A, B],
            [C, D,  -0.354],
            [E, 0.612, F]])
R2 = R.T

print(R*R2)
print(R.det())
