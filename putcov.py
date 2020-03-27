#!/usr/bin/python3

for i in open("kmerres.txt"):
	fields = i.rstrip().split("\t")
	try:
		cov = open("output/" + fields[3] + ".cov")
		coverage = cov.readline().rstrip()
		cov.close()
	except FileNotFoundError:
		coverage = "total_coverage"
	fields.append(coverage)
	print("\t".join(fields))
