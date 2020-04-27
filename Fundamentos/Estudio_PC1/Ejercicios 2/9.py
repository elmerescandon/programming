import numpy as np
import rotaciones as r

R = np.array([[0.7905,  0.6046, 0.0977],
              [-0.3864, 0.3686, 0.8455],
              [0.4752, -0.7061, 0.5250]])
RINV = R.T

q = r.quaterion(R)
RT = r.rquater(q)
th, ej = r.ejeang(R)
R2 = r.rodr(th, ej)
qinv = r.quaterion(RINV)
RPRUEBA = r.rquater(qinv)

print(RINV)
print(RPRUEBA)
