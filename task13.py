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

fig, axs = plt.subplots(2, sharex=True)

for i in range(np.size(n)):
    r, P, E = rad.radial(l, n[i], Z, False)
    rl, Pl, El, Gl = radlog.radiallog(l, n[i], Z, False)
    Elis.append(E)
    Logis.append(El)
    GridPoints.append(Gl)
    R.append(rl)
    if i == 1:
        axs[0].plot(np.sqrt(r), P)
        axs[1].plot(np.sqrt(rl), np.sqrt(rl)*Pl)


Elis = np.array(Elis)
Logis = np.array(Logis)

Realis = -(Z**2)/(2*np.power(n,2))

print(Elis)
print(Logis)
print(Realis)

print(GridPoints)

fig.supxlabel('$\sqrt{\mathrm{r}}$ (a.u.)')
axs[0].set_title("Linear")
axs[1].set_title("Logarithmic")
fig.suptitle('Radial Functions 2s for $Z=1$')

fig.savefig('fleeble.pdf')

plt.show()
