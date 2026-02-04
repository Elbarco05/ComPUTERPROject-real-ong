import radial
import radial as rad
import radiallog as radlog
import Radial_functions as Rf
import numpy as np
import matplotlib.pyplot as plt


l = 0
n = np.array([1, 2, 3])
Z = 1

fig, axs = plt.subplots(np.size(n))

for i in range(np.size(n)):
    r, P, E = rad.radial(l, n[i], Z, False)
    axs[i].plot(r, P)

    # Expectation values
    dr = r[1] - r[0]
    r_exp_val = np.sum(r*P**2) * dr
    axs[i].vlines(r_exp_val, np.min(P), np.max(P), linestyle="dashed", color = "red")


plt.show()
