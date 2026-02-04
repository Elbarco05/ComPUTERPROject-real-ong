import matplotlib.pyplot as plt
import radiallog as RL


Na_11_plot = 0
Na_11_excited1_plot = 0
Na_11_excited2_plot = 0

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

if Na_11_excited1_plot:
    l = 2
    n = 3
    Z = 11
    N = 11
    a = 0.2683

    r, P, E = RL.radiallog(a, N, l, n, Z)


plt.show()





