#!/usr/bin/python3

import sys

rna = dict()
for i in open(sys.argv[1]):
	if i.startswith("#"):
		continue
	cols = i.rstrip().split("\t")
	scf  = cols[0]
	pos  = cols[1]
	ref  = cols[3]
	alt  = cols[4]
	if len(ref) > 1 or len(alt) > 1:
		continue
	key = "%s:%s:%s" % (scf, pos, alt)
	rna[key] = [0, i]

for i in open(sys.argv[2]):
	if i.startswith("#"):
		continue
	cols = i.rstrip().split("\t")
	scf  = cols[0]
	pos  = cols[1]
	alt  = cols[4]
	key = "%s:%s:%s" % (scf, pos, alt)
	if key in rna:
		rna[key][0] = 1

total = 0
good  = 0
#out_matched = open("dnamatched.vcf", "w")
#out_novel   = open("dnanotmatched.vcf", "w")
for key in rna:
	if rna[key][0] == 1:
		good += 1
		#out_matched.write(rna[key][1])
	else:
		#out_novel.write(rna[key][1])
		pass
	total += 1

print("Total:", total, "\nGood:", good)
#out_matched.close()
#out_novel.close()
