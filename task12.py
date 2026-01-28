import Radial_functions as Rf
import radial as rad
import radiallog as radlog
import numpy as np
import matplotlib.pyplot as plt

rads = 1
pots = 0




r = np.linspace(0.001,20,1000)
Z = 1
P1 = Rf.P3s(r,Z)
P2 = Rf.P3p(r,Z)
P3 = Rf.P3d(r,Z)

if rads:
    plt.plot(r,P1**2)
    plt.plot(r,P2**2)
    plt.plot(r,P3**2)

def V(r, l):
    return -Z/r + (l*(l+1))/(2*r**2)


if pots:
    V1 = V(r,0)
    V2 = V(r,1)
    V3 = V(r,2)
    plt.plot(r,V1)
    plt.plot(r,V2)
    plt.plot(r,V3)
    plt.ylim(-0.5,0.05)



plt.show()
