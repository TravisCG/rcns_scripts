#!/usr/bin/python3

"""
  Merge fasta files with spacer (fill with Ns)
"""

import sys

def revcomp(seq):
	tr = str.maketrans('ATGC', 'TACG')
	return (seq[::-1].translate(tr))

files = list()
for paramindex in range(len(sys.argv[1:])):
	if paramindex % 2 == 0:
		files.append([sys.argv[paramindex+1], ''])
	else:
		files[-1][1] = sys.argv[paramindex+1]

for frecord in files:
	f = open(frecord[0])
	f.readline()
	seq = ''
	for i in f:
		seq += i.rstrip()
	f.close()
	if frecord[1] == 'R':
		seq = revcomp(seq)
	print(seq + 'N' * 1000, end = '')
