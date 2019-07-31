#!/usr/bin/python3

"""
   Quick and dirty VCF comparator
"""

import sys

def vcf2set(filename):
	store = set()
	fl = open(filename)
	for i in fl:
		if i.startswith("#"):
			continue
		fields = i.rstrip().split("\t")
		fields[0] = fields[0].replace('chr', '')
		if len(fields[3]) != 1 or len(fields[4]) != 1:
			continue
		store.add("%s_%s_%s_%s" % (fields[0], fields[1], fields[3], fields[4]))
	fl.close()
	return(store)

a = vcf2set(sys.argv[1])
b = vcf2set(sys.argv[2])

print("\n".join(list(a - b)))
#print(len(a.intersection(b)), len(a), len(b))
#print("\n".join(list(a.intersection(b))))
