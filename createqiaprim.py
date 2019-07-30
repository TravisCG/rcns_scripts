#!/usr/bin/python3

"""
   Create QIAGene primer txt file, which
   is necessary to run the pipeline.
   Usualy this file can be downloaded,
   but in the case of custom panels,
   the user can download only a bed
   file. This script extracts the
   sequences from the reference file
   and creates the corrisponding input file.
"""

import sys

def revcomp(txt):
	tr = str.maketrans('ATGC', 'TACG')
	return(txt[::-1].translate(tr))

ref = dict()
for i in open(sys.argv[1]):
	if i.startswith(">"):
		idx = i.split()[0][1:]
		ref[idx] = list()
	else:
		ref[idx].append(i.rstrip())

for i in ref:
	ref[i] = "".join(ref[i])

bed = open(sys.argv[2])
bed.readline()
for i in bed:
	fields = i.rstrip().split("\t")
	chrx   = fields[0]
	start  = int(fields[1]) - 1
	end    = int(fields[2]) - 1
	ori    = fields[5]
	if ori == '-':
		seq = ref[chrx][start-20:start]
		print("%s\t%d\t0\t%s" % (chrx, start-1, seq))
	else:
		seq = ref[chrx][end:end+20]
		print("%s\t%d\t1\t%s" % (chrx, end, revcomp(seq)))
