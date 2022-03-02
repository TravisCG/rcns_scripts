#!/usr/bin/python3

import sys
import re

rre = re.compile("([^:]+):(\d+)-(\d+)")

regions = dict()
for i in open(sys.argv[1]):
	r = i.rstrip().split("\t")[0]
	match = rre.search(r)
	if match:
		chrx  = match.group(1)
		start = int(match.group(2))
		end   = int(match.group(3))
		if chrx not in regions:
			regions[chrx] = list()
		regions[chrx].append([start, end])

samplename = list()
vcf = open(sys.argv[2])
header = vcf.readline().rstrip().split()
for h in header[9:]:
	samplename.append(h)

for i in vcf:
	cols = i.rstrip().split("\t")
	chrx = cols[0]
	pos  = int(cols[1])
	for j in range(9,len(cols)):
		sample = cols[j]
		if len(cols[3]) != 1 or len(cols[4]) != 1:
			continue
		gt = sample.split(":")[0]
		if chrx in regions:
			for r in regions[chrx]:
				if pos > r[0] and pos < r[1]:
					print(chrx, r[0], r[1], gt, samplename[j - 9])	
