# %% Inicializar librerías
import numeric as num
import symbolic as sym
import numpy as np
import sympy as sp

# %% Inicializar variables
q1,q2,q3 = sp.symbols(r'q_1 q_2 q_3')
cos = sp.cos
sin = sp.sin
x = sp.Matrix([[cos(q1)+cos(q2)+cos(q3)],
               [sin(q1)+sin(q2)+sin(q3)]])
q = sp.Matrix([q1,q2,q3])
J = x.jacobian(q)
display(J)
