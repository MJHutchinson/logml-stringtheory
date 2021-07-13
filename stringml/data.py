import ast
import glob

import numpy as np


def get_geometry_ids(data_folder="data/bundle_solutions"):
    return [
        int(f.split("/")[-1].split(".")[0]) for f in glob.glob(data_folder + "/*.txt")
    ]


def load_vector_bundle_solutions_txt(id, data_folder="data/bundle_solutions"):
    with open(f"{data_folder}/{id}.txt") as f:
        data = f.readlines()

    s = "".join(data)
    s = s.replace("\n", "")
    s = s.replace("{", "[")
    s = s.replace("}", "]")
    s = ast.literal_eval(s)
    s = np.array(s)

    return s


def load_vector_bundle_solutions_npy(id, data_folder="data/bundle_solutions"):
    return np.load(f"{data_folder}/{id}.npy")


def flatten_solutions(solutions):
    return np.reshape(solutions, (solutions.shape[0], -1))


def reduce_solutions(solutions):
    return solutions[..., :-1]
