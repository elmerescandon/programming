import numpy as np
import rotaciones as r

R1 = r.rot(-90, 'z')
R2 = r.rot(90, 'x')

R = R1.dot(R2)
