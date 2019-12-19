#!/usr/bin/python3

"""
  Merge fasta files with spacer (fill with Ns)
"""

import sys
import glob

files = glob.glob("*.fasta")

for frecord in files:
	f = open(frecord)
	f.readline()
	seq = ''
	for i in f:
		seq += i.rstrip()
	f.close()
	print(seq + 'N' * 1000, end = '')
