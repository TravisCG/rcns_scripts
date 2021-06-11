#!/usr/bin/python3

import sys

table = open(sys.argv[1])
table.readline()
exphash = dict()
for i in table:
	cols = i.rstrip().split("\t")
	if cols[0] not in exphash:
		exphash[cols[0]] = list()
	exphash[cols[0]].append(cols[1])

for i in exphash:
	print("python3 ../onepeak.py ../peakandsummitandmotifpos.tsv " + i + " " + " ".join(exphash[i]) + " >" + i + ".tsv")
