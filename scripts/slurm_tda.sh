#!/bin/bash

# Usage: `sbatch`

#SBATCH --job-name=stringML-tda
#SBATCH --partition=zzi-medium
#SBATCH --cpus-per-task=1
#SBATCH --time=14-00:00:00
#SBATCH --mem=25G
#SBATCH --ntasks=1
#SBATCH --output=slurm_logs/persistent_homology

#SBATCH --array=1-51%6

id=awk 'NR==$SLURM_ARRAY_TASK_ID' data/bundle_solutions/_ids.txt
limit_solutions=100
data_path=/home/mhutchin/Documents/projects/logml-stringtheory/data/bundle_solutions
results_path=/home/mhutchin/Documents/projects/logml-stringtheory/results/persitent_homology
fig_path=/home/mhutchin/Documents/projects/logml-stringtheory/figures/persistent_homology

python scripts/tda.py \
    $id \
    --limit_solutions $limit_solutions \
    --save_figs True \
    --data_path $data_path \
    --results_path $results_path \
    --fig_path $fig_path
