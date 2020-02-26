#!/usr/bin/python3

"""
  ./createantimo.py antiinmotif.tsv antibodypermotif | tee colsumanti.tsv
"""

import sys

f = open(sys.argv[1])
f.readline()
allantibodies = set()
tables = dict()
for i in f:
	fields = i.rstrip().split("\t")
	antibody = fields[1]
	motifpos = fields[2]
	motif    = fields[3]

	allantibodies.add(antibody)
	if motif not in tables:
		tables[motif] = dict()
	if motifpos not in tables[motif]:
		tables[motif][motifpos] = set()
	tables[motif][motifpos].add(antibody)

outdir = sys.argv[2]
allantibodies = list(allantibodies)
print("motif\tmotifposcount", "\t".join(allantibodies), sep = "\t")
for motif in tables:
	out = open(outdir + "/" + motif + ".tsv", "w")
	out.write("motifpos\t" + "\t".join(allantibodies) + "\n")
	colsums = [0] * len(allantibodies)
	motifposcount = 0
	for motifpos in tables[motif]:
		outline = list()
		outline.append(motifpos)
		for index in range(0, len(allantibodies)):
			if allantibodies[index] in tables[motif][motifpos]:
				outline.append("1")
				colsums[index] += 1
			else:
				outline.append("0")
		out.write("\t".join(outline) + "\n")
		motifposcount += 1
	out.close()
	print(motif, motifposcount, "\t".join([str(x) for x in colsums]), sep = "\t")
