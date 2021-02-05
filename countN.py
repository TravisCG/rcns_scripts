#!/usr/bin/python3

import sys

seqs = dict()

for i in open(sys.argv[1]):
	if i.startswith('>'):
		idx = i.rstrip()[1:]
		seqs[idx] = list()
	else:
		seqs[idx].append(i.rstrip())

for i in seqs:
	countN = 0
	total  = 0
	for j in seqs[i]:
		total += len(j)
		for k in range(len(j)):
			if j[k] == 'N':
				countN += 1
	print(i, total, countN)
