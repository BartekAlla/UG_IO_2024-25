import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import numpy as np

options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=my_bounds)
optimizer.optimize(fx.sphere, iters=1000)
