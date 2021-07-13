# %%
%load_ext autoreload
%autoreload 2

import os
os.chdir('/home/mhutchin/Documents/projects/logml-stringtheory')

from stringml.data import get_geometry_ids, load_vector_bundle_solutions_npy, reduce_solutions, flatten_solutions
from stringml.tda import tda

results_folder = "results/persitent_homology"
# %%

ids = get_geometry_ids()
id = ids[0]

solutions = load_vector_bundle_solutions_npy(id)
solutions = flatten_solutions(reduce_solutions(solutions))

# %%
# Too many solutions can run out of memory, need to run on a bigger computer
limit_solutions = 1_000
tda(id, limit_solutions=limit_solutions)
# %%
