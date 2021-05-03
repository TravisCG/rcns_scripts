#!/usr/bin/python3

"""
   Calculate the average peak score per antibody-motif pairs
"""

import sys

matrix = dict()
allantibody = set()
allmotifs = set()

inputtable = open(sys.argv[1])
inputtable.readline()

for i in inputtable:
	columns   = i.rstrip().split("\t")
	motif     = columns[0]
	antibody  = columns[5]
	peakscore = float(columns[8])
	summith   = float(columns[7])
	if motif not in matrix:
		matrix[motif] = dict()
	if antibody not in matrix[motif]:
		matrix[motif][antibody] = [0.0, 0.0]
	allantibody.add(antibody)
	allmotifs.add(motif)
	matrix[motif][antibody][0] += peakscore
	matrix[motif][antibody][1] += 1.0

allmotifs = list(allmotifs)
allantibody = list(allantibody)
print("motif\t" + "\t".join(allantibody))

for motif in allmotifs:
	out = list()
	out.append(motif)
	for antibody in allantibody:
		if motif not in matrix or antibody not in matrix[motif]:
			mean = 0.0
		else:
			values = matrix[motif][antibody]
			mean = values[0] / values[1]
		out.append(str(mean))
	print("\t".join(out))
