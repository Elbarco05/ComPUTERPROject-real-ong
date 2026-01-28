import numpy as np
import matplotlib.pyplot as plt
import Radial_functions as Rf


r = np.linspace(0,20,1000)
Z = 1
P1s = Rf.P1s(r,Z)
P3s = Rf.P3s(r,Z)
P3p = Rf.P3p(r,Z)
P3d = Rf.P3d(r,Z)

def rad_dens(func):     #radial density is just P(r)**2
    return func**2

def V_eff(r,l):     #effective potential with the Q.number l (for ang.mom)
    return -Z/r + (l*(l +1))/(2*r**2)

s_pot = V_eff(r, 0)
p_pot = V_eff(r, 1)
d_pot = V_eff(r, 2)


rad_dens_plots = 1
V_eff_plots = 1

if rad_dens_plots:
    plt.figure()
    plt.title("Radial density for different orbitals")
    #plt.plot(r, rad_dens(P1s))
    plt.plot(r, rad_dens(P3s), label = '3s')
    plt.plot(r, rad_dens(P3p), label = '3p')
    plt.plot(r, rad_dens(P3d), label = '3d')
    plt.ylabel('D(r)')
    plt.xlabel('r')
    plt.legend()
    plt.grid()

if V_eff_plots:
    plt.figure()
    plt.title("Effective potential for different orbitals")
    plt.plot(r, s_pot, label = 's')
    plt.plot(r, p_pot, label = 'p')
    plt.plot(r, d_pot, label = 'd')
    plt.ylim(-0.5, 0.4)
    plt.ylabel('V(r)')
    plt.xlabel('r')
    plt.legend()
    plt.grid()


plt.show()

























