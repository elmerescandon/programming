# %% Inicializar librerías
import numeric as num
import symbolic as sym
import numpy as np
import sympy as sp

# %% Inicializar variables
q1,q2,l1,l2 = sp.symbols(r'q_1 q_2 l_1 l_2')
cos = sp.cos

sin = sp.sin
pos = sp.Matrix([[l1*cos(q1) + l2*cos(q1+q2)],
                 [l1*sin(q1) + l2*sin(q1+q2)],
                 [q1+q2]])
J_g = sp.Matrix([[-l1*sin(q1) - l2*sin(q1+q2),-l2*sin(q1+q2)],
                 [l1*cos(q1) + l2*cos(q1+q2),l2*cos(q1+q2)],
                 [0,0],
                 [0,0],
                 [0,0],
                 [1,1]])
display(J_g.shape)
fx,fy,fz,ux,uy,uz = sp.symbols(r'f_x f_y f_z u_x u_y u_z')
F = sp.Matrix([[fx],[fy],[fz],[ux],[uy],[uz]])
tau = J_g.T*F
display(sp.simplify(tau))
