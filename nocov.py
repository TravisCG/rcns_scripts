#!/usr/bin/python3

import sys

genome = dict()

for i in open(sys.argv[1]):
	fields = i.rstrip().split("\t")
	target = fields[5]
	tlen   = int(fields[6])
	start  = int(fields[7])
	end    = int(fields[8])
	
	if target not in genome:
		genome[target] = [0] * tlen
	for j in range(start - 1, end):
		genome[target][j] = 1
print("chromosome", "number_of_Ns", "percentage_of_Ns", "coverage%")
for chrom in genome:
	count = 0
	for i in genome[chrom]:
		if i == 0:
			count += 1
	print(chrom, count, count / len(genome[chrom]), 100.0 - (count / len(genome[chrom]) * 100.0))
