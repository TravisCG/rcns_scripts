#!/usr/bin/python3

import sys

def overlapcalc(start1, end1, start2, end2):
	"""
	Calculate overlapping percentage between two interval.
	It is ssumps start1 < start2
	"""
	endh     = max(end1, end2)
	endl     = min(end1, end2)
	total    = endh - start1
	overlap  = endl - start2
	overperc = float(overlap) / float(total)
	return(overperc)

minsim = float(sys.argv[2])

intervals = dict()
experiments = set()
peakfile = open(sys.argv[1])
peakfile.readline()
for i in peakfile:
	fields = i.rstrip().split()
	experiments.add(fields[0])
	chrx   = fields[1]
	start  = int(fields[2])
	end    = int(fields[3])
	if chrx not in intervals:
		intervals[chrx] = list()
	intervals[chrx].append((start, end))
peakfile.close()

for i in intervals:
	sreg = sorted(intervals[i], key = lambda x: x[0])
	intervals[i] = list()
	intervals[i].append( (sreg[0][0], sreg[0][1]) )
	for j in range(1,len(sreg)):
		if sreg[j][0] < sreg[j-1][1]:
			# overlap
			overperc = overlapcalc(sreg[j-1][0], sreg[j-1][1], sreg[j][0], sreg[j][1])
			if overperc > minsim:
				continue
			intervals[i].append( (sreg[j][0], sreg[j][1]) )

peakfile = open(sys.argv[1])
header = list(experiments)
print("\t".join(header))
peakfile.readline()

for i in peakfile:
	fields = i.rstrip().split("\t")
	chrx   = fields[1]
	start  = int(fields[2])
	end    = int(fields[3])
	for j in intervals[chrx]:
		if j[0] < start:
			overperc = overlapcalc(j[0], j[1], start, end)
			if overperc > minsim:
				table[]
		else:
			break
