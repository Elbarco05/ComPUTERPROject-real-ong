import matplotlib.pyplot as plt
import numpy as np
import radiallog as RL


l1 = 0
l2 = 1
l3 = 2

n1 = 3
Z1 = 11
N1 = 11
a1 = 0.2683

r1, P1, E1 = RL.radiallog(a1, N1, l1, n1, Z1)
r2, P2, E2 = RL.radiallog(a1, N1, l2, n1, Z1)
r3, P3, E3 = RL.radiallog(a1, N1, l3, n1, Z1)

Na_11_plot = 0
Na_11_excited1_plot = 0
Na_11_excited2_plot = 0
all_plots = 1

if all_plots:
    plt.figure()
    plt.title("Radial functions of Na for ground and excited config")
    plt.plot(r1,np.sqrt(r1)*P1, label = 'ground config')
    plt.plot(r2, np.sqrt(r2) * P2, label='first excited')
    plt.plot(r3, np.sqrt(r3) * P3, label='second excited')
    plt.ylabel('p')
    plt.xlabel('r')
    plt.xlim(0, 40)
    plt.legend()
    plt.grid()

if Na_11_plot:
    l = 0
    n = 3
    Z = 11
    N = 11
    a = 0.2683

    r, P, E = RL.radiallog(a, N, l, n, Z)

if Na_11_excited1_plot:
    l = 1
    n = 3
    Z = 11
    N = 11
    a = 0.2683

    r, P, E = RL.radiallog(a, N, l, n, Z)

if Na_11_excited2_plot:
    l = 2
    n = 3
    Z = 11
    N = 11
    a = 0.2683

    r, P, E = RL.radiallog(a, N, l, n, Z)


plt.show()








