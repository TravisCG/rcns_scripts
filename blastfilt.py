#!/usr/bin/python3

"""
   Very simple blast filter
"""

import sys

seqlen = dict()
slfile = open(sys.argv[1])
slfile.readline()
for i in slfile:
	sid, sl = i.rstrip().split()
	seqlen[sid] = int(sl)

for i in open(sys.argv[2]):
	if i.startswith("#"):
		continue
	fields = i.rstrip().split("\t")
	qid = fields[0]
	hid = fields[1]
	alen = int(fields[3])

	if qid in seqlen:
		if alen > seqlen[qid] * 0.90:
			print(i,end="")
	if hid in seqlen:
		if alen > seqlen[hid] * 0.90:
			print(i,end="")
