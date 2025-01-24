#!/usr/bin/python3

import sys

gene = dict()

for i in open(sys.argv[1]):
	fields = i.rstrip().split("\t")
	gene[fields[0]] = fields[1]

for i in open(sys.argv[2]):
	fields = i.rstrip().split()
	genename = "_".join(fields[0].split("_")[0:-1])
	if genename in gene:
		print(i.rstrip(),gene[genename], sep = "\t")
	else:
		print(i.rstrip(),"null", sep = "\t")
