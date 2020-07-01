# -*- coding: utf-8 -*-

import numpy as np
import sympy as sp
from sympy.matrices import Matrix

L,phi_1,phi_2,phi_3,phi_4,r,vx,vy,theta = sp.symbols(r'L \dot{\phi_{1}} \dot{\phi_{2}} \dot{\phi_{3}} \dot{\phi_{4}} r v_x v_y \dot{theta}')


A = Matrix([[0,-1,-L],
			[1,0,-L],
			[0,1,-L],
			[-1,0,-L]])

twist = Matrix([[vx],[vy],[theta]])
rueda_vel = Matrix([[phi_1],[phi_2],[phi_3],[phi_4]])
direct = (r)*(A.pinv())*rueda_vel
inversa = (1/r)*A*twist

print("Cinemática Directa\n")
sp.pprint(sp.simplify(direct))
print("Cinemática Inversa\n")
sp.pprint(sp.sympify(inversa))
print("\n")



preg_a = direct.subs([(r, 0.08), (L, 0.2), (phi_1, 0.5), (phi_2,-0.5), (phi_3, 0.5),(phi_4, -0.5)])
print(preg_a)