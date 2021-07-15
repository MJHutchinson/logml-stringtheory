import os
import sys
import glob
import pickle

from ripser import ripser
from persim import plot_diagrams

from stringml.data import (
    load_vector_bundle_solutions_npy,
    reduce_solutions,
    flatten_solutions,
)

import matplotlib.pyplot as plt


def persistent_homology(
    id,
    max_homology=1,
    limit_solutions=None,
    save_figs=True,
    data_folder="data/bundle_solutions",
    results_folder="results/persitent_homology",
    figures_folder="figures/persitent_homology",
):
    """Computes the persistent homology for the valid vector bundle
    solutions for a given ID CY manifold. Saves the results to a pickle
    and if specified saves the plots.

    limit_solutions limits the number of solutions used to compute the PH to save on time.
    """
    data = load_vector_bundle_solutions_npy(id, data_folder=data_folder)
    data = flatten_solutions(reduce_solutions(data))
    n = data.shape[0]

    results_folder = f"{results_folder}/{max_homology}"
    figures_folder = f"{figures_folder}/{max_homology}"
    os.makedirs(results_folder, exist_ok=True)
    if save_figs:
        os.makedirs(figures_folder, exist_ok=True)

    if (limit_solutions is not None) and (n > limit_solutions):
        data = data[:limit_solutions]
        resutls_file = f"{results_folder}/{id}_{limit_solutions}_{n}.pkl"
        figure_file = f"{figures_folder}/{id}_{limit_solutions}_{n}.pdf"
    else:
        resutls_file = f"{results_folder}/{id}.pkl"
        figure_file = f"{figures_folder}/{id}.pdf"

    if not os.path.isfile(resutls_file):
        persistent_homology = ripser(data, maxdim=max_homology)
        pickle.dump(persistent_homology, open(resutls_file, "wb"))
    else:
        print(
            f"Skipping computation for {id} {limit_solutions}, results already exist."
        )
        sys.exit(0)

    if save_figs:
        diagrams = persistent_homology["dgms"]
        plot_diagrams(diagrams, show=False)
        plt.savefig(figure_file)


def load_persistent_homology_results(id, results_folder="results/persitent_homology"):
    """Loads the most compleate set of persistent homology results for
    a given CY manifold (by most solutions used to compute the PH)
    """

    all_results = sorted(glob.glob(f"{results_folder}/{id}*"))
    all_results = [f.split(".")[0].split("/")[-1] for f in all_results]

    if int(all_results[0]) == int(id):
        load_file = f"{all_results[0]}.pkl"
    else:
        max_computed = max([int(f.split("_")[1]) for f in all_results])
        n = int(all_results[0].split("_")[2])
        load_file = f"{id}_{max_computed}_{n}.pkl"

    return pickle.load(open(f"{results_folder}/{load_file}", "rb"))
