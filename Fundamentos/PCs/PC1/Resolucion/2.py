import numpy as np
import rotaciones as r

p_r1 = np.array([[2.16], [-0.1], [0.3]])
print("P1 con respecto a R\n", p_r1)

p_rl = np.array([[0.12], [-0.1], [0.3]])
p2 = np.array([[2.44], [0.889], [0]])
R_rl2 = r.rot(-30, 'y')

p_r2 = p_rl + R_rl2.dot(p2)
print("P2 con respecto a R\n", p_r2)

p3 = np.array([[2.9358], [-1.695], [0]])
R_rl3 = r.rot(-50, 'y')

p_r3 = p_rl + R_rl3.dot(p3)
print("P3 con respecto a R\n", p_r3)

# Parte B


q_ir = np.array([[0.94], [0], [0], [0.34]])
R_ir = r.rquater(q_ir)

R_ri = R_ir.T
p_ri = np.array([[-5], [2], [0.2]])


T_ri = r.transmaxtrix(R_ri, p_ri)
T_ir = np.linalg.inv(T_ri)

p_i1 = r.vect_tmatrix(T_ri, p_r1)
p_i2 = r.vect_tmatrix(T_ri, p_r2)
p_i3 = r.vect_tmatrix(T_ri, p_r3)
print("Vector p1 con respecto al sistema inercial:\n", p_i1)
print("Vector p2 con respecto al sistema inercial:\n", p_i2)
print("Vector p3 con respecto al sistema inercial:\n", p_i3)
