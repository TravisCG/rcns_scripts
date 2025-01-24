#!/usr/bin/python3

"""
   Read motif pos (actually a BED file) and select variations which
   can be found inside the motif
"""

import sys

motifregion = dict()

regionfile = open(sys.argv[1])
regionfile.readline() # read header
for i in regionfile: # read motif region
	cols = i.rstrip().split("\t")
	chrx = cols[0]
	start = int(cols[1])
	end = int(cols[2])
	strand = cols[3]

	if chrx not in motifregion:
		motifregion[chrx] = list()
	motifregion[chrx].append([start,end,strand])

for i in open(sys.argv[2]): # read variation file
	cols = i.rstrip().split()
	chrx = cols[0]
	pos  = int(cols[1])
	if chrx in motifregion:
		for j in motifregion[chrx]:
			print(j[0],j[1])
			if pos > j[0] and pos < j[1]:
				print(chrx, j[0], j[1], j[2], pos)
