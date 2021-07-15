import os
import click

from stringml.data import (
    load_vector_bundle_solutions_npy,
    flatten_solutions,
    reduce_solutions,
    get_geometry_ids,
)
from stringml.tda import persistent_homology

base_path = "."

data_path = base_path + "/data/bundle_solutions"
results_path = base_path + "/results/persitent_homology"
fig_path = base_path + "/figures/persitent_homology"


def get_data(id):
    data = load_vector_bundle_solutions_npy(id, data_path)
    data = flatten_solutions(reduce_solutions(data))
    return data


@click.command()
@click.argument("id", type=int)
@click.option(
    "--max_homology",
    type=int,
    default=1,
    help="max homology to evaluate",
)
@click.option(
    "--limit_solutions",
    type=int,
    default=0,
    help="limit the number of solutions to use to compute the TDA. 0 uses all solutions",
)
@click.option(
    "--save_figs",
    type=bool,
    default=False,
    help="save the plots of the persistent homology",
)
@click.option(
    "--data_path",
    type=str,
    default=data_path,
    help="path to the bundle solutions",
)
@click.option(
    "--results_path",
    type=str,
    default=results_path,
    help="path to the results folder",
)
@click.option(
    "--fig_path",
    type=str,
    default=fig_path,
    help="path to the figures folder",
)
def compute_persistent_homology(
    id, max_homology, limit_solutions, save_figs, data_path, results_path, fig_path
):
    data = get_data(id)
    os.makedirs(results_path, exist_ok=True)
    if save_figs:
        os.makedirs(fig_path, exist_ok=True)
    persistent_homology(
        id,
        max_homology=max_homology,
        limit_solutions=None if limit_solutions == 0 else limit_solutions,
        save_figs=save_figs,
        data_folder=data_path,
        results_folder=results_path,
        figures_folder=fig_path,
    )


if __name__ == "__main__":
    compute_persistent_homology()
