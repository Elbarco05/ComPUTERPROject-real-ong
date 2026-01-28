import radial as rad
import radiallog as radlog
import Radial_functions as Rf
import numpy as np
import matplotlib.pyplot as plt



l = 0
n = np.array([1, 2, 3, 6, 9])
Z = 1

Elis = []
Logis = []
GridPoints = []
R = []
PP = []

fig, axs = plt.subplots(np.size(n))

for n_ in n:
    r, P, E = rad.radial(l, n_, Z, False)
    rl, Pl, El, Gl = radlog.radiallog(l, n_, Z, False)
    Elis.append(E)
    Logis.append(El)
    GridPoints.append(Gl)
    R.append(rl)

Elis = np.array(Elis)
Logis = np.array(Logis)

Realis = -(Z**2)/(2*np.power(n,2))

axs[0].plot()

print(Elis)
print(Logis)
print(Realis)

print(GridPoints)
