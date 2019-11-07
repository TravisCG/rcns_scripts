#!/usr/bin/python3

"""
   Rename fasta contigs using the filename
"""

import sys

name = sys.argv[1].replace(".fasta", "_")
contig = 1

for i in open(sys.argv[1]):
    if i.startswith(">"):
        print(">" + name + str(contig))
        contig += 1
    else:
        print(i.rstrip())
