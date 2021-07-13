import pickle

from ripser import ripser
from persim import plot_diagrams

from stringml.data import (
    load_vector_bundle_solutions_npy,
    reduce_solutions,
    flatten_solutions,
)

import matplotlib.pyplot as plt


def tda(
    id,
    limit_solutions=None,
    save_figs=True,
    data_folder="data/bundle_solutions",
    results_folder="results/persitent_homology",
    figures_folder="figures/persitent_homology",
):
    data = load_vector_bundle_solutions_npy(id, data_folder=data_folder)
    data = flatten_solutions(reduce_solutions(data))

    if limit_solutions is not None:
        data = data[:limit_solutions]
        resutls_file = f"{results_folder}/{id}_{limit_solutions}.pkl"
        figure_file = f"{figures_folder}/{id}_{limit_solutions}.pdf"
    else:
        resutls_file = f"{results_folder}/{id}.pkl"
        figure_file = f"{figures_folder}/{id}.pdf"

    persistent_homology = ripser(data)
    pickle.dump(persistent_homology, open(resutls_file, "wb"))

    if save_figs:
        diagrams = persistent_homology["dgms"]
        plot_diagrams(diagrams, show=False)
        plt.savefig(figure_file)
