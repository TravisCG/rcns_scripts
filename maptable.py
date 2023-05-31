#!/usr/bin/python3

"""
   Create a table from a bunch of samtools flagstat files.
"""

import sys

def get_map_percent(filename):
	f = open(filename)
	for i in range(7):
		f.readline()
	rawperc = f.readline().rstrip().split(" ")[5]
	perc = rawperc[1:len(rawperc)-1]
	f.close()
	return float(perc) / 100.0

table = dict()
header = set()
for i in sys.argv[1:]:
	chunks = i.rstrip(".stat").split("_")
	genome = chunks[0] + "_" + chunks[1]
	sample = "_".join(chunks[2:])
	perc = get_map_percent(i)
	header.add(genome)
	if sample not in table:
		table[sample] = dict()
	table[sample][genome] = perc

header = list(header)
print("\t".join(header))
for t in table:
	line = []
	line.append(t)
	for h in header:
		line.append(str(table[t][h]))
	print("\t".join(line))
