import pyswarms as ps
import numpy as np
import math
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

def endurance(position):
    x, y, z, u, v, w = position
    return -(math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w))

def f(swarm):
    return np.array([endurance(particle) for particle in swarm])

options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=my_bounds)
optimizer.optimize(f, iters=1000)

cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()
