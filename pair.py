#!/usr/bin/python3

import sys

antibody = dict()
for i in open(sys.argv[1]):
	fields = i.rstrip().split("\t")
	antibody[fields[1]] = fields[2:]

for i in open(sys.argv[2]):
	fields = i.rstrip().split("\t")
	print(i.rstrip(), "\t".join(antibody[fields[1]]),sep="\t")
