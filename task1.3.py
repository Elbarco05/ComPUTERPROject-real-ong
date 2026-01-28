import numpy as np
import matplotlib.pyplot as plt
import Radial_functions as Rf
import radial as Rad
import radiallog as RL

#Parameters and Q.numbers
l = 0
n = 1
Z = 1

#r, P, E = RL.radiallog(l1, n1, Z)

n1_plots = 1
n2_plots = 0
n3_plots = 0
n6_plots = 0
n9_plots = 0

if n1_plots:
    l1 = 0
    n1 = 1

    r, P, E = Rad.radial(l1, n1, Z)
    r, P, E = RL.radiallog(l1, n1, Z)

if n2_plots:
    l1 = 0
    n2 = 2

    r, P, E = Rad.radial(l1, n2, Z)
    r, P, E = RL.radiallog(l1, n2, Z)

if n3_plots:
    l1 = 0
    n3 = 3

    r, P, E = Rad.radial(l1, n3, Z)
    r, P, E = RL.radiallog(l1, n3, Z)

if n6_plots:
    l1 = 0
    n6 = 6

    r, P, E = Rad.radial(l1, n6, Z)
    r, P, E = RL.radiallog(l1, n6, Z)

if n9_plots:
    l1 = 0
    n9 = 9

    r, P, E = Rad.radial(l1, n9, Z)
    r, P, E = RL.radiallog(l1, n9, Z)

plt.show()

"log version of the radial goes quicker"