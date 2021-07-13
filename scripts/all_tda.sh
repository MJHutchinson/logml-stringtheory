limit_solutions=100
data_path=/home/mhutchin/Documents/projects/logml-stringtheory/data/bundle_solutions
results_path=/home/mhutchin/Documents/projects/logml-stringtheory/results/persitent_homology
fig_path=/home/mhutchin/Documents/projects/logml-stringtheory/figures/persistent_homology

while read id; do
    python scripts/tda.py \
    $id \
    --limit_solutions $limit_solutions \
    --save_figs True \
    --data_path $data_path \
    --results_path $results_path \
    --fig_path $fig_path
done < data/bundle_solutions/_ids.txt