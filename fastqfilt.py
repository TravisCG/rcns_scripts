#!/usr/bin/python3

import sys
import gzip

reads = set()

for i in open(sys.argv[1]):
	reads.add(i.rstrip())

counter = 0
out = False
for i in gzip.open(sys.argv[2]):
	if counter % 4 == 0:
		idx = i.decode('utf-8').rstrip().split()[0][1:]
		if idx in reads:
			out = True
		else:
			out = False
		counter = 0
	if out:
		print(i.decode('utf-8').rstrip())
	counter += 1
