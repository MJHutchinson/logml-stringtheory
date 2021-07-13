import click

from stringml.data import (
    load_vector_bundle_solutions_npy,
    flatten_solutions,
    reduce_solutions,
    get_geometry_ids,
)
from stringml.tda import tda

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
def compute_tda(id, limit_solutions, save_figs, data_path, results_path, fig_path):
    data = get_data(id)
    tda(
        id,
        limit_solutions=None if limit_solutions == 0 else limit_solutions,
        save_figs=save_figs,
        data_folder=data_path,
        results_folder=results_path,
        figures_folder=fig_path,
    )


if __name__ == "__main__":
    compute_tda()
