import rotaciones as r
import numpy as np

R = r.rot(90, 'y').dot(r.rot(45, 'z'))
p = np.array([[1],
              [1],
              [1]])
fp = R.T.dot(p)
print(np.round(fp, 2))
