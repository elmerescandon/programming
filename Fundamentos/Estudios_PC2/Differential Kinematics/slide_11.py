import sympy as sp
from sympy.matrices import Matrix
import numpy as np
import rotaciones as r

sp.init_printing()
theta, theta_dot = sp.symbols(r'\theta \dot{\theta}')
Ry = r.srot(theta, 'y')
Rydot = Ry.diff(theta)
w_skew = sp.simplify(Rydot*theta_dot*Ry.T)
w_skew
