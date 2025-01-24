#!/usr/bin/python3

import sys

for i in open(sys.argv[1]):
	cols = i.rstrip().split("\t")
	for j in range(1,len(cols)):
		print(cols[0], cols[j])
