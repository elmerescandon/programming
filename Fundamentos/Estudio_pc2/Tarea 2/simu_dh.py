from serialrobot import *
import numpy as np

# Longitudes iniciales
# Se ponen las variables en (dm) - decímetros
l1 = 1.35
l2 = 1.35
l3 = 0.38
l4 = 1.20
l6 = 0.95
l7 = 0.18
# Th = [d1, th1, a1, alpha1, rp1]
# Definición del robot usando parámetros DH
# Orden: d, th, a, alpha, PR
Th = [[l1,          0,  0, (np.pi/2), 'r'],
      [0,   (np.pi/2), l2,        0, 'r'],
      [0,           0, l3, (np.pi/2), 'r'],
      [l4,    (np.pi),  0, (np.pi/2), 'r'],
      [0,     (np.pi),  0, (np.pi/2), 'r'],
      [l6,    (np.pi), l7,        0, 'r']]
meca500 = SerialRobot(Th, 'Meca500')
q = [0, 0, 0, 0, 0, 0]
T = meca500.fkine(q)
print(np.round(T, 3))

# Cinemática directa (posición inicial) =====================================
q = np.deg2rad([0, 0, 0, 0, 0, 0])
T = meca500.fkine([0, 0, 0, 0, 0, 0])
print(np.round(T))

# Visualización (de la posición inicial) =====================================
q = np.deg2rad([0, 0, 0, 0, 0, 0])
fig = plt.figure("Home")
meca500.plot(q)

# Recoger un Objeto
q = np.deg2rad([0, -40, -40, -60, -30, 50])
fig = plt.figure("Recoger")
meca500.plot(q)

#
q = np.deg2rad([0, -30, 0, 0, 90, 180])
fig = plt.figure()
meca500.plot(q)

#
q = np.deg2rad([30, -90, 60, -30, 20, -90])
fig = plt.figure("Posición 4")
meca500.plot(q)
plt.show()
