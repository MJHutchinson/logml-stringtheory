# %%
%load_ext autoreload
%autoreload 2

import os
os.chdir('/data/ziz/not-backed-up/mhutchin/logml-stringtheory')

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from stringml.data import get_geometry_ids, load_vector_bundle_solutions_npy, reduce_solutions, flatten_solutions

data_folder="data/bundle_solutions"
results_folder="results/persitent_homology"
figures_folder="figures/persitent_homology"
# %%
ids = get_geometry_ids(data_folder=data_folder)
solutions = load_vector_bundle_solutions_npy(ids[1], data_folder=data_folder)
# %%
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
# %%
# processed_solutions = flatten_solutions(reduce_solutions(solutions))
processed_solutions = flatten_solutions(solutions)
pca = PCA(9).fit(processed_solutions)
# %%
kmeans = KMeans(n_clusters=10).fit(processed_solutions)
# %%
id = ids[]
solutions = load_vector_bundle_solutions_npy(id, data_folder=data_folder)
processed_solutions = flatten_solutions(solutions)
processed_solutions = processed_solutions[np.random.permutation(solutions.shape[0])]
limit = 1000
processed_solutions = processed_solutions[:limit]
distances = np.abs(processed_solutions[:, np.newaxis, :, np.newaxis] - processed_solutions[np.newaxis, :, np.newaxis, :]).sum(axis=(2,3))
sns.histplot(distances.flatten())
plt.title(id)
# %%
limit = 1000
for id in ids:
    print(id)
    solutions = load_vector_bundle_solutions_npy(id, data_folder=data_folder).astype(np.int8)
    solutions = solutions[np.random.permutation(solutions.shape[0])]
    solutions = solutions[:limit]
    processed_solutions = flatten_solutions(solutions)
    distances = np.abs(processed_solutions[:, np.newaxis, :, np.newaxis] - processed_solutions[np.newaxis, :, np.newaxis, :]).sum(axis=(2,3))
    sns.histplot(distances.flatten())
    plt.title(f'{id} solutions used: {solutions.shape[0]}')
    plt.savefig(f'results/distance_analysis/{id}_{solutions.shape[0]}.pdf')


# %%
