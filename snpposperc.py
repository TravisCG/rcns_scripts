#!/usr/bin/python3

import sys

def transcriptperc(ranges, pos, minindex, maxindex):
	midindex = int(minindex + (maxindex - minindex) / 2)
	if midindex == minindex or midindex == maxindex:
		if pos > ranges[minindex][0] and pos < ranges[minindex][1]:
			midindex = minindex
		if pos > ranges[maxindex][0] and pos < ranges[maxindex][1]:
			midindex = maxindex
		if pos > ranges[midindex][0] and pos < ranges[midindex][1]:
			perc = float(pos - ranges[midindex][0]) / float(ranges[midindex][1] - ranges[midindex][0])
			if ranges[midindex][2] == "-":
				perc = 1.0 - perc
			return perc
		return 0.0
	if pos > ranges[minindex][0] and pos < ranges[midindex][1]:
		return transcriptperc(ranges, pos, minindex, midindex)
	if pos > ranges[midindex][1] and pos < ranges[maxindex][1]:
		return transcriptperc(ranges, pos, midindex, maxindex)
	return 0.0

gff = dict()
for i in open(sys.argv[1]):
	cols = i.rstrip().split()
	if cols[2] == "transcript":
		if cols[0] not in gff:
			gff[cols[0]] = list()
		gff[cols[0]].append([int(cols[3]), int(cols[4]), cols[6]])

for contig in gff:
	gff[contig] = sorted(gff[contig], key = lambda x: x[0])

for i in open(sys.argv[2]):
	cols = i.rstrip().split()
	contig = cols[0]
	pos = int(cols[1])
	if contig not in gff:
		continue
	percent = transcriptperc(gff[contig], pos, 0, len(gff[contig])-1)
	if percent > 0.0:
		print(percent)
