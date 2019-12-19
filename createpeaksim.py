#!/usr/bin/python3

import sys

peaks = dict()

table = open(sys.argv[1])
table.readline()
for i in table:
	f = i.rstrip().split("\t")
	chrx  = f[0] + ":" + f[1]
	start = int(f[2])
	end   = int(f[3])
	if start > end:
		sys.err("Bro, something wrong with the coordinates!" + i)
		exit(0)
	if chrx not in peaks:
		peaks[chrx] = list()
	peaks[chrx].append((start, end))

for chrx in peaks:
	for i in range(len(peaks[chrx]) - 1):
		for j in range(i+1, len(peaks[chrx])):
			distance = abs(peaks[chrx][j][0] - peaks[chrx][i][1])
			print(distance)
