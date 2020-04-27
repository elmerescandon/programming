import numpy as np
import rotaciones as r

R1 = r.rot(90, 'z')
R2 = r.rot(30, 'y')
R3 = r.rot(45, 'z')
R = (R1.dot(R2)).dot(R3)
R = np.round(R, 2)
print(R)
