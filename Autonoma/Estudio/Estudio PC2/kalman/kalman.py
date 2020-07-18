import numpy as np
import matplotlib.pyplot as plt

class Sistema1d(object):
    def __init__(self, dt):
        self.dt = dt   # Valor inicial de X
        self.X = 20    # Perturbación "real" del sistema
        self.e = np.sqrt(0.01);
        self.d = np.sqrt(100);   # Los sensores son poco confiables en este modelo
        # Parámetros del
        self.A=1; self.B=dt; self.Ne=1; self.C=1;

    def get_measurement(self, u):
        """
        Retorna la medición de la posición (usando un "GPS")
        """
        # Dinámica "real" del sistema
        self.X = self.A*self.X + self.B*u + self.Ne*(self.e*np.random.normal())
        # Medición del sistema
        Zmed = self.C*self.X + (self.d*np.random.normal())
        return Zmed

    def get_state(self):
        """
        Retorna el valor real de la posición (solo para evaluar el resultado)
        """
        return self.X

# Parámetros del sistema
dt = 0.1

# Matrices de la dinámica del sistema y de la medición
A = 1
B = dt
Ne = 1
C = 1

# Matrices de covarianza
R = 0.01    # "Confiabilidad" del modelo del sistema
Q = 10     # "Confiabilidad" de la medición (ejemplo: 10m -> Q=10^2)

# Inicialización del estado y de su covarianza
x = 1000    # Valor inicial
P = 100  # Incertidumbre inicial (ejemplo: +-10 -> P=10^2)

# Alocación de memoria para las trayectorias
tt = np.arange(0, 10, dt)
Xreal_tr = np.zeros(len(tt))
xtr = np.zeros(len(tt))
ztr = np.zeros(len(tt))
Ptr = np.zeros(len(tt))


sistema = Sistema1d(dt)

# Bucle principal
for i in range(len(tt)):
    # Tiempo
    t = tt[i]
    # Señal de control
    u = 1
    # Medición usando GPS (xreal es solo para evaluación, no se utiliza)
    zmed = sistema.get_measurement(u)
    #zmed, xreal = medicion1d(dt, xreal, u)

    # Filtro de Kalman: Predicción
    x = A*x + B*u
    P = A*P*A + Ne*R*Ne
    # Filtro de Kalman: Corrección
    K = P*C*(Q+C*P*C)**(-1)
    x = x + K*(zmed-C*x)
    P = P - K*C*P

    #Almacenar datos
    Xreal_tr[i] = sistema.get_state()
    xtr[i] = x
    ztr[i] = zmed
    Ptr[i] = P

# Gráficos
plt.plot(tt, Xreal_tr)
plt.plot(tt, xtr)
plt.plot(tt, ztr)
plt.plot(tt, Xreal_tr+3*np.sqrt(Ptr), 'y')
plt.plot(tt, Xreal_tr-3*np.sqrt(Ptr), 'y')
plt.legend(['$x_{real}$', '$x_{est}$', '$z_{med}$'])
plt.grid()
plt.show()
