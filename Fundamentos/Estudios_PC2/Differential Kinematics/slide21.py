import sympy as sp
from sympy.matrices import Matrix
import numpy as np
import rotaciones as r


def skew2vec(w_hat):
    return sp.Matrix([w_hat[2, 1], w_hat[0, 2], w_hat[1, 0]])


# Método 2
# Calcular la matriz de rotación equivalente
# Encontrar w^ = Rdot*R.T
# Obtener w_x,w_y,w_z del w skew
sp.init_printing()
phi_r, phi_p, phi_y, dr, dp, dy = sp.symbols(
    r'\phi_{r} \phi_{p} \phi_{y} \dot{\phi_{r}} \dot{\phi_{p}} \dot{\phi_{y}}')
Rz = r.srot(phi_r, 'z')
Ry = r.srot(phi_p, 'y')
Rx = r.srot(phi_y, 'x')
R = sp.simplify(Rz*Ry*Rx)
R_dot = sp.simplify(sp.diff(R, phi_r)*dr + sp.diff(R, phi_p)*dp + sp.diff(R, phi_y)*dy)
w_skew = sp.simplify(R_dot*R.T)
skew2vec(w_skew)
