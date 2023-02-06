#!/usr/bin/python3

"""
  GFA converter to FASTA collection. Read a bounch of GFA files and create
  a concatenated FASTA file, with file name prefix, so there is no name
  collision.
"""

import sys
import os

def readGFA(filename):
	prefix = os.path.basename(filename).replace(".bp.p_ctg.gfa","_")
	for i in open(filename):
		line = i.rstrip().split()
		if line[0] == "S":
			print(">" + prefix + line[1])
			print(line[2])

for i in sys.argv[1:]:
	readGFA(i)
