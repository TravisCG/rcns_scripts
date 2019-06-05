#!/usr/bin/python3

"""
   Quick and dirty way to filter VCF and create a binary matrix
"""

import sys

for i in open(sys.argv[1]):
	if i.startswith("##"):
		continue
	fields = i.rstrip().split("\t")
	if i.startswith("#"):
		print("\t".join(fields[39:]))
	if fields[6] != "PASS":
		continue
	if len(fields[3]) != 1 or len(fields[4]) != 1:
		continue
	row = list()
	row.append("%s_%s_%s_%s" % (fields[0], fields[1], fields[3], fields[4]))
	freq = 0
	for j in range(39,71):
		gt = fields[j].split(":")[0]
		if gt == './.':
			row.append('0')
		elif gt == '0/1':
			row.append('1')
			freq += 1
		elif gt == '1/1':
			row.append('2')
			freq += 1
		else:
			print(gt)
			sys.exit(1)
	if freq < 2:
		continue
	print("\t".join(row))
