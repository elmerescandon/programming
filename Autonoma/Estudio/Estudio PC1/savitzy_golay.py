import numpy as np
from matplotlib import pyplot as plt
ts = 0.01
t = np.array([38, 39, 40, 41, 42])*ts
# Ecuación de Polinomio
A = np.array([np.ones(5).T, t, t**2, t**3, t**4]).T
# Resultados de X
y = np.array([[92.5], [92.9], [93.1], [92.8], [91.3]])
# Coeficientes
x = np.round(np.linalg.inv(A).dot(y), 2)
a0 = x[0, 0]
a1 = x[1, 0]
a2 = x[2, 0]
a3 = x[3, 0]
a4 = x[4, 0]
# Polinomio de 2do grado
print("El polinomio buscado es: q(t) = {} + {} t + {} t^2 +{} t^3 + {} t^4 ".format(a0, a1, a2, a3, a4))
t_ref = t[2]
q_dot = a1 + 2*a2*t_ref + 3*a3*(t_ref**2) + 4*a4*(t_ref**3)
print(q_dot)

# Gráfica
plt.plot(t, y, 'o')
tt = np.linspace(0.37, 0.43, 50)
qq = a0 + a1*tt + a2*tt**2 + a3*tt**3 + a4*tt**4
td = 0.4
qd = 93.1
dqq = qd + q_dot*(tt-td)
plt.plot(tt, qq)
plt.plot(tt, dqq)
plt.show()
