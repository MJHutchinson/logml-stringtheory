#!/bin/bash

#SBATCH --job-name=stringMLtda
#SBATCH --partition=ziz-large
#SBATCH --time=8:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=25G 
#SBATCH --cpus-per-task=1
#SBATCH --output=slurm_logs/persistent_homology/%A_%a.out
#SBATCH --error=slurm_logs/persistent_homology/%A_%a.err

#SBATCH --array=1-51%20

source venv/bin/activate

data_path=data/bundle_solutions
results_path=results/persitent_homology
fig_path=figures/persistent_homology

com=NR==$SLURM_ARRAY_TASK_ID
id=$(awk $com $data_path/_ids.txt)
limit_solutions=10000
max_homology=2

python scripts/tda.py \
    $id \
    --max_homology $max_homology \
    --limit_solutions $limit_solutions \
    --save_figs True \
    --data_path $data_path \
    --results_path $results_path \
    --fig_path $fig_path
