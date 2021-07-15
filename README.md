# LogML Summer School - String theory classification project

This repo contains a small package wlongside some scripts to look at valid line bundles over Calabi-Yao manifolds

## Getting started
Running `setp.sh` should do everything you need, if you have python 3.8 and `virtualenv` installed. 

If not, then you shoudl set up in the way you want to have your environment set, then install the package in this repo via `pip install -e .` and then the requirements in the `requirments.txt` file (via `pip install -r requirements.txt`).

## Structure
### stringml
This is the basic library. At the moment contains some utils for loading the line bundle solutions from files, and code to run persistent homology analysis.

### data
Contains various pieces of data

### notebooks
Contains various notebooks of messing around. May not be clean

### scripts
Contains command line python scripts to dispatch analyses, as well as wrapper bash scripts to run over all geometries, both on a single machine and parallel processed SLURM.

### figures / results
Contains various figures and results from experiments run


## TDA
The TDA part of the library at the minute contains code to do the following:
- Persistent Homology analysis

Precomputed results for the persistent homology analysis can be found in the results folder, with the pictures in the figures folder. results can be loaded using the applicable method in the package.

Results are save with the name `[geometry id]_[number of solutions]_[max solutions]`, wherer the numebr of solutions is limited to prevent memory overflow. If all the solutions were used then it is just saved as `[geometry id]`. Using the appropriate load function in th elibrary will load the ost compleate set of results avalible. 