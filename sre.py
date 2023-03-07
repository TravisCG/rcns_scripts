#!/usr/bin/python3

"""
replace sample id in VCF
"""

import sys

d = {}
for i in open(sys.argv[1]):
	cols = i.rstrip().split()
	d[cols[0]] = cols[1]

for i in open(sys.argv[2]):
	if i.startswith("#CHROM"):
		# replace header
		newheader = []
		for j in i.rstrip().split():
			if j in d:
				newheader.append(d[j])
			else:
				newheader.append(j)
		print("\t".join(newheader))
	else:
		print(i.rstrip())
