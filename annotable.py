#!/usr/bin/python3

import sys
import re

yeastre = re.compile("([^|]+_YEAST)")
table = dict()
print("uniprot", end = "")
for filename in sys.argv[1:]:
	print("\t" + filename, end = "")
	gff = open(filename)
	for line in gff:
		cols = line.split("\t")
		if len(cols) < 3 or cols[1] != "blastx" or cols[2] != "protein_match":
			continue
		match = yeastre.search(line)
		if match:
			protname = match.group(1)
			if protname not in table:
				table[protname] = dict()
			if filename not in table[protname]:
				table[protname][filename] = 0
			table[protname][filename] += 1
print()
for protname in table:
		print(protname, end = "")
		for filename in sys.argv[1:]:
			if filename in table[protname]:
				print("\t", table[protname][filename], sep = "", end = "")
			else:
				print("\t0", end = "")
		print()
