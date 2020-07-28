import rotaciones as r
import numpy as np
import sympy as sp
from sympy.matrices import Matrix

# L = d,theta, a, aplha 'r/p'
x1, x2, x3, x4, x5, x6, q1, q2, q3 = sp.symbols(r'x_1 x_2 x_3 x_4 x_5 x_6 q_1 q_2 q_3')
L = [[x1, q1, x4, sp.pi/2, 'r'],
     [x2, q2, x5, 0, 'r'],
     [x3, q3, x6, 0, 'r']]
T, J = r.jacob_g(L)
J
J_t = J.subs({x1: 0, x2: 0, x3: 0, x4: 0})
J.shape
sp.simplify((J_t.T*J_t).det())

# Obtención de singularidades
J_a = J_t[0:3, 0:3]
J_a
sp.simplify(J_a.det())
J_b = J_t[3:6, 0:3]
J_b

# Obtener la velocidad de la configuracion
# vd < (0.5,0.5,0.5)
# wd < (1,1,1)
# qi = (90,0,-90)
# Deteterminar la velocidad angular mínima para cada motor,
# pueda alcancer las velocidades deseadas
# Asumir a3 = a2 = 1m

# Obtener jacobiano con los valores de q iniciales
J_d = J.subs(({x1: 0, x2: 0, x3: 0, x4: 0, x5: 1, x6: 1, q1: sp.pi/2, q2: 0, q3: -sp.pi/2}))


# Obtener valores de q a partir de Velocidad Lineal
Jd_v = J_d[0:3, 0:3]
vd = Matrix([[0.5], [0.5], [0.5]])
q_vd = Jd_v.pinv()*vd  # Este es el que funciona!!1
J_d*q_vd
# # Obtener valores de q a partir de Velocidad angular
Jd_w = J_d[3:6, 0:3]
wd = Matrix([[0.8], [0.8], [0.8]])
q_wd = Jd_w.pinv()*wd
q_wd
twist_w = J_d*q_wd
twist_w


# Inciso E
f1, f2, f3, m1, m2, m3 = sp.symbols(r'f_1 f_2 f_3 m_1 m_2 m_3')
F = Matrix([[f1], [f2], [f3], [m1], [m2], [m3]])
F
J_d.T*F
