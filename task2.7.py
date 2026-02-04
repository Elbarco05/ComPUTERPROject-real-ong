import matplotlib.pyplot as plt
import radiallog as RL

Li_3_plot = 0

if Li_3_plot:
    l = 0
    n = 2
    Z = 3
    N = 3
    a = 0.28326672      #Increase in a gives a increase in energy

    r, P, E = RL.radiallog(a, N, l, n, Z)

plt.show()