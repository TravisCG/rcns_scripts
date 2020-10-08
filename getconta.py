#!/usr/bin/python3

"""
   I try to filter out contamination
   This script reads a blast result file
   and print out potential contaminations
"""

import sys

for i in open(sys.argv[1]):
	if i.startswith("#"):
		continue
	fields = i.rstrip().split()
	seqlen = float(fields[0].split("_")[3])
	alnlen = float(fields[3])
	if alnlen / seqlen > 0.1:
		print(fields[0])
