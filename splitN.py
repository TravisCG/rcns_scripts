#!/usr/bin/python3

"""
   Split large sequences by N
   It is working only with single fasta file
"""

import sys

seq = list()
collect = False
for i in open(sys.argv[1]):
	if i.startswith('>'):
		collect = True
		continue
	if collect:
		seq.append(i.rstrip())

newseq = "".join(seq).split("N")
count  = 1

for s in newseq:
	if len(s) > 0:
		print(">",count,"\n",s, sep = "")
		count += 1

