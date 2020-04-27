import numpy as np
import rotaciones as r
c = np.cos
s = np.sin

rx = r.rot(10, 'x')
ry = r.rot(70, 'y')
rz = r.rot(30, 'z')
R = rx.dot(ry).dot(rz)


t1 = np.deg2rad(10)
t2 = np.deg2rad(70)
t3 = np.deg2rad(30)
R2 = np.array([[c(t1)*c(t3),                                     c(t2)*s(t3),     -s(t2)],
               [s(t1)*s(t2)*c(t3)-c(t1)*s(t3), s(t1)*s(t2)*s(t3)+c(t1)*c(t3), s(t1)*c(t2)],
               [c(t1)*s(t2)*c(t3)+s(t1)*s(t3), c(t1)*s(t2)*s(t3)-s(t1)*c(t3), c(t1)*c(t2)]])


th2 = np.arctan2(R[0, 2], -np.sqrt(R[1, 2]**2 + R[2, 2]**2))
th1 = np.arctan2(-R[1, 2]/np.cos(th2), R[2, 2]/np.cos(th2))
th3 = np.arctan2(-R[0, 1]/np.cos(th2), R[0, 0]/np.cos(th2))
print(R)

th1d = np.rad2deg(th1)
th2d = np.rad2deg(th2)
th3d = np.rad2deg(th3)
R3 = r.rot(th1d, 'x').dot(r.rot(th2d, 'y')).dot(r.rot(th3d, 'z'))
print(th1d, th2d, th3d)
print(R2)
print(R3)
