import numpy as np
import rotaciones as r

R = r.rot(-90, 'z').dot(r.rot(90, 'y'))
print(np.round(R, 2))
