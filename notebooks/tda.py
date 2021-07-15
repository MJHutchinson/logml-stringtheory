# %%
%load_ext autoreload
%autoreload 2

import os
os.chdir('/data/ziz/not-backed-up/mhutchin/logml-stringtheory')

from stringml.data import get_geometry_ids, load_vector_bundle_solutions_npy, reduce_solutions, flatten_solutions
from stringml.tda import tda

data_folder="data/bundle_solutions"
results_folder="results/persitent_homology"
figures_folder="figures/persitent_homology"
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

for id in ids:
    print(load_vector_bundle_solutions_npy(id).shape)

# %%
id=6225
all_results = sorted(glob.glob(f"{results_folder}/{id}*"))
all_results = [f.split('.')[0].split('/')[-1] for f in all_results]
if int(all_results[0]) == int(id):
    load_file = f"{all_results[0]}.pkl"
else:
    max_computed = max([int(f.split('_')[1]) for f in all_results])
    n = int(all_results[0].split("_")[2])
    load_file = f"{id}_{max_computed}_{n}.pkl"

print(load_file)
# %%
