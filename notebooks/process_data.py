# %%
%load_ext autoreload
%autoreload 2

from stringml.data import load_vector_bundle_solutions_txt, get_geometry_ids
# %%

data_folder = "../data/bundle_solutions"
ids = get_geometry_ids(data_folder)

for id in ids:
    print(id)
    data = load_vector_bundle_solutions_txt(id, data_folder)
    np.save(f.replace('txt', 'npy'), data)
# %%
