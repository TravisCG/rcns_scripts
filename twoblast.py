#!/usr/bin/python3

import sys

scaffolds = dict()

for i in open(sys.argv[1]):
	if i.startswith("#"):
		continue
	fields = i.rstrip().split("\t")
	if fields[0] not in scaffolds:
		scaffolds[fields[0]] = [float(fields[11]), 0.0]

for i in open(sys.argv[2]):
	if i.startswith("#"):
		continue
	fields = i.rstrip().split("\t")
	if fields[0] not in scaffolds:
		scaffolds[fields[0]] = [0.0,0.0]
	if scaffolds[fields[0]][1] == 0:
		scaffolds[fields[0]][1] = float(fields[11])

for i in scaffolds:
	print(i, scaffolds[i][0], scaffolds[i][1])
