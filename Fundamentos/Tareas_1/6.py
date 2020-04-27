import numpy as np
import rotaciones as r
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


R21 = r.rot(-53, 'x').dot(r.rot(180, 'z'))
R03 = r.rot(-90, 'y').dot(r.rot(-143, 'x'))
R01 = r.rot(-90, 'y').dot(r.rot(90, 'x'))

R23 = R21.dot(R01.T).dot(R03)
print(np.round(R23, 2))
