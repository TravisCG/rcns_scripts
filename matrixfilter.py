#!/usr/bin/python3

import sys

for i in open(sys.argv[1]):
	if i.startswith("ID"):
		print(i.rstrip())
		continue
	cols = i.rstrip().split("\t")
	tags = cols[0].split("_")
	if len(tags[3]) > 1 and len(tags[4]) > 1:
		continue
	summ = 0
	for j in range(1, len(cols)):
		if cols[j] == ".":
			cols[j] = "0"
		summ = summ + int(cols[j])
	if summ == 0:
		continue
	print("\t".join(cols))
