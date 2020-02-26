#!/usr/bin/python

import sys

inp = open(sys.argv[1])
inp.readline()
cc = dict()

for i in inp:
	f = i.rstrip().split("\t")
	if f[0] not in cc:
		cc[f[0]] = set()
	cc[f[0]].add(float(f[1]))
inp.close()

final = dict()
for chem in cc:
	l = list(cc[chem])
	l = sorted(l)
	final[chem] = dict()
	count = 1
	for i in l:
		final[chem][str(i)] = str(count)
		count += 1

inp = open(sys.argv[1])
print(inp.readline().rstrip(), "cc_category", sep = "\t")

for i in inp:
	f = i.split("\t")
	category = final[f[0]][str(float(f[1]))]
	print(i.rstrip(), category, sep = "\t")
