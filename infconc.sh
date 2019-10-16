#!/bin/bash

# Salmonella infantis concatenated core genes multiple alignment

#SBATCH -A rbgma
#SBATCH --job-name=together
#SBATCH --time=168:00:00
#SBATCH -n 8

cd /big/scratch/pez5mnr/salmonella/genes_concatenated
../progressiveMauve --output-guide-tree=concatenated.genes.guide_tree --output=concatenated *.fasta >log.txt 
