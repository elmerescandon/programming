
import numpy as np


def attractive_pot(q, qf, d, zeta=1):
    dist = np.linalg.norm(q-qf)
    if (dist <= d):
        U = 0.5*zeta*dist*dist
        f = -zeta*(q-qf)
    else:
        U = d*zeta*dist - 0.5*zeta*d*d
        f = -d*zeta*(q-qf)/dist
    return U, f


def repulsive_pot(q, qobst, rho, eta=1, Umax=1):
    # This considers a point obstacle at qobst
    dist = np.linalg.norm(q-qobst)
    if (dist <= rho):
        if (dist == 0):
            U = 100
            f = np.zeros(2,)
        else:
            U = 0.5*eta*(1.0/dist-1.0/rho)**2
            f = eta*(1.0/dist-1.0/rho)*(1/dist**2)*(q-qobst)/dist
        if (U > Umax):
            U = Umax
    else:
        U = 0
        f = np.zeros(2,)
    return U, f


def repulsive_pots(q, qobst, rho, eta=1, Umax=1):
    # This considers point obstacles at qobst
    Utot = 0
    ftot = np.zeros(2,)
    for i in range(len(qobst)):
        U, f = repulsive_pot(q, qobst[i,:], rho, eta, Umax)
        Utot += U
        ftot += f
    return Utot, ftot
