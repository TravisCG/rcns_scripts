#!/usr/bin/python3

"""
   Filter peakscore.tsv
   Remove peak positions which
   can be found only in one experiment
"""

import sys

peaks = dict()

peakfile = open(sys.argv[1])
print(peakfile.readline().rstrip()) # print out header
for i in peakfile:
	fields = i.rstrip().split()
	motifposid = fields[3]
	antibody = fields[1]
	if motifposid not in peaks:
		peaks[motifposid] = dict()
	if antibody not in peaks[motifposid]:
		peaks[motifposid][antibody] = list()
	peaks[motifposid][antibody].append(i.rstrip())

for motifposid in peaks:
	if len(peaks[motifposid]) > 1:
		for antibody in peaks[motifposid]:
			for entry in peaks[motifposid][antibody]:
				print(entry)
