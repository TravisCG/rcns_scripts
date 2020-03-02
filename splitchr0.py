#!/usr/bin/python3

"""
   chr0 in our rabbit denovo is too big for most of the
   bioinformatic programs. So this script slice it to
   smaller parts
"""

import sys

seq = list()
collect = False
for i in open(sys.argv[1]):
	if i.startswith('>chr0'):
		collect = True
		continue
	if not collect:
		print(i.rstrip())
	else:
		seq.append(i.rstrip())
newseq = "".join(seq).split("N"*1000)
count = 1
for i in newseq:
	if len(i) > 1:
		print(">chr0_" + str(count))
		print(i)
		count += 1
