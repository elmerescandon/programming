# -*- coding: utf-8 -*-

import numpy as np

q0 = 20 # ang. inicial
qf = 80 # ang.final
t = 4 # Tiempo total
vf = 5 # Grados/s

# Ecuación matricial 

q = np.array([[20],[80],[0],[5]])
A = np.array([[0,0,0,1],
			  [64,16,4,1],
			  [0,0,1,0],
			  [48,8,1,0]])

coefs = np.linalg.inv(A).dot(q)
print(coefs)