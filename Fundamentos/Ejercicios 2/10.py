import numpy as np
import rotaciones as r

R = r.rot(90, 'x')
q = r.quaterion(R)
RT = r.rquater(q)
print(q)
print(np.round(R, 2))
print(np.round(RT, 2))
