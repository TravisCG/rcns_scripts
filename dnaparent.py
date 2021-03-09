#!/usr/bin/python3

import sys

vcf = open(sys.argv[1])
#vcf.readline()
for i in vcf:
	cols = i.rstrip().split("\t")
	mother = cols[9].split(":")[0]
	father = cols[18].split(":")[0]
	print(cols[0], cols[1], mother, father)
