import radiallogsequel as radlog
import Radial_functions as Rf
import numpy as np
import matplotlib.pyplot as plt

l = np.array([0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0])
n = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5])
Z = 11
a = 0.2683
N = 11

E = np.zeros(np.size(l))

for i in range(np.size(l)):
    r, P, E_, g = radlog.radiallog(l[i], n[i], Z, a, N)
    E[i] = E_

Ediff = np.zeros(np.size(l)-3)

E0 = 2*E[0] + 2*E[1] + 6*E[2]
for i in range(np.size(l)-3):
    Ediff[i] = E0 + E[i+3] - (E0 + E[3])

print(E)
print(np.sort(Ediff))
