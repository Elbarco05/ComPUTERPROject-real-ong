import numpy as np
import matplotlib.pyplot as plt
import Radial_functions as Rf



r = np.linspace(0,20,1000)
Z = 1
P1s = Rf.P1s(r,Z)   #importing radial wave functions
P2s = Rf.P2s(r,Z)
P3s = Rf.P3s(r,Z)
P3p = Rf.P3p(r,Z)
P3d = Rf.P3d(r,Z)


def rad_dens(func):     #radial density is just P(r)**2
    return func**2

def r_expectation_value(funcy):     #Expectation value of r
    dr = r[1] - [0]
    return sum(r*funcy**2) * dr

rad_dens_plots3s = 0
rad_dens_plots3p = 0
rad_dens_plots3d = 0
rad_dens_plots1s_2s_num = 0
rad_dens_plots1s_2s_ana = 0


if rad_dens_plots3s:
    plt.figure()
    plt.title("Radial density for 3s")
    plt.plot(r, rad_dens(P3s), label='3s')
    plt.vlines(r_expectation_value(P3s), np.max(P3s), np.min(P3s), label='expectation val 3s', color='orange')
    plt.ylabel('D(r)')
    plt.xlabel('r')
    plt.legend()
    plt.grid()

if rad_dens_plots3p:
    plt.figure()
    plt.title("Radial density for 3p")
    plt.plot(r, rad_dens(P3p), label='3p')
    plt.vlines(r_expectation_value(P3p), np.max(P3p), np.min(P3p), label='expectation val 3p', color='orange')
    plt.ylabel('D(r)')
    plt.xlabel('r')
    plt.legend()
    plt.grid()

if rad_dens_plots3d:
    plt.figure()
    plt.title("Radial density for 3d")
    plt.plot(r, rad_dens(P3d), label='3d')
    plt.vlines(r_expectation_value(P3d), np.max(P3d), np.min(P3d), label='expectation val 3d', color='orange')
    plt.ylabel('D(r)')
    plt.xlabel('r')
    plt.legend()
    plt.grid()

if rad_dens_plots1s_2s_num:
    plt.figure()
    plt.title("Radial density for different orbitals with numerical expectation value")
    plt.plot(r, rad_dens(P1s), label='1s', color='blue')
    plt.plot(r, rad_dens(P2s), label='2s', color='orange')
    plt.vlines(1.4999999, np.max(P1s), np.min(P1s), label='expectation val 1s', color='blue', linestyle = 'dashed')
    plt.vlines(5.9999999, np.max(P2s), np.min(P2s), label='expectation val 2s', color='orange', linestyle = 'dashed')
    plt.ylabel('D(r)')
    plt.xlabel('r')
    plt.legend()
    plt.grid()

if rad_dens_plots1s_2s_ana:
    plt.figure()
    plt.title("Radial density for different orbitals with analytical expectation value")
    plt.plot(r, rad_dens(P1s), label='1s', color='blue')
    plt.plot(r, rad_dens(P2s), label='2s', color='orange')
    plt.vlines(1.5, np.max(P1s), np.min(P1s), label='expectation val 1s', color='blue', linestyle = 'dashed')
    plt.vlines(6, np.max(P2s), np.min(P2s), label='expectation val 2s', color='orange', linestyle = 'dashed')
    plt.ylabel('D(r)')
    plt.xlabel('r')
    plt.legend()
    plt.grid()


#Radial expectation value 3s = 13.499999
#Radial expectation value 3p = 12.499999
#Radial expectation value 3d = 10.499999

plt.show()
    plt.grid()



plt.show()
