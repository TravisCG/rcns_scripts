#!/usr/bin/python3

"""
   Merging expression tables. The tables contain gene abundances from
   different genome builds.
"""

import sys

table = dict()
allsamples = set()

for filename in sys.argv[1:]:
	f = open(filename)
	header = f.readline().rstrip().split()
	allsamples.update(header[1:])
	for row in f:
		cols = row.rstrip().split("\t")
		gene = cols[0]
		if gene not in table:
			table[gene] = dict()
		for i in range(1, len(cols)):
			sample = header[i]
			table[gene][sample] = cols[i]
	f.close()
allsamples = list(allsamples)
print("\t".join(allsamples))
for i in table:
	if len(allsamples) == len(table[i]):
		row = list()
		row.append(i)
		zero = 0
		for s in allsamples:
			row.append(table[i][s])
			if table[i][s] == "0":
				zero += 1
		if zero < len(allsamples):
			print("\t".join(row))
