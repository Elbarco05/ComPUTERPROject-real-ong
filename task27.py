import radiallogsequel as radlog
import Radial_functions as Rf
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

l = np.array([0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0])
n = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5])
Z = 3
N = 3

a = 0.1

def energies(a):
    E = np.zeros(np.size(l))

    for i in range(np.size(l)):
        r, P, E_, g = radlog.radiallog(l[i], n[i], Z, a, N, False)
        E[i] = E_

    Ediff = np.zeros(np.size(l) - 1)

    E0 = 2 * E[0] + E[1]
    for i in range(np.size(l) - 1):
        Ediff[i] = E0 + E[i + 1] - (E0 + E[1])

    Ediff = np.sort(Ediff)

    return Ediff

def diff(a):

    E = np.zeros(np.size(l))

    for i in range(np.size(l)):
        r, P, E_, g = radlog.radiallog(l[i], n[i], Z, a, N, False)
        E[i] = E_

    Ediff = np.zeros(np.size(l)-1)

    E0 = 2*E[0] + E[1]
    for i in range(np.size(l)-1):
        Ediff[i] = E0 + E[i+1] - (E0 + E[1])

    Ediff = np.sort(Ediff)

    Ediffcomp = np.array([0, 0.0679061, 0.1239602, 0.1409064, 0.1425362, 0.1595267,
                          0.1661675,  0.1668684, 0.166899,  0.1745054])

    spongebob = 0

    for i in range(np.size(Ediff)):
        spongebob += (Ediff[i] - Ediffcomp[i])**2

    return spongebob


opt_a, err = opt.leastsq(diff, 0.2683)[:2]
opt_a = opt_a[0]
elis_a = 0.28326672

print(opt_a)
print(diff(opt_a))
print(diff(0.28326672))

print(energies(opt_a))
print(energies(elis_a))
