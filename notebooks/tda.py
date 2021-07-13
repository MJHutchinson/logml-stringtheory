# %%
%load_ext autoreload
%autoreload 2

import os
os.chdir('/home/mhutchin/Documents/projects/logml-stringtheory')

import ast
import numpy as np

from ripser import ripser

from stringml.data import get_geometry_ids, load_vector_bundle_solutions_npy, reduce_solutions, flatten_solutions
# %%

ids = get_geometry_ids()
id = ids[0]

solutions = load_vector_bundle_solutions_npy(id)
solutions = flatten_solutions(reduce_solutions(solutions))

# %%
# Too many solutions can run out of memory
limit_solutions = 10_000
persistent_homology = ripser(solutions[:limit_solutions])
# %%
