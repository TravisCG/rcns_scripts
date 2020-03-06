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
# we need 10 pices
seqc = len(newseq)
merge = int(seqc / 10)

count = 1
for i in range(seqc):
	if i % merge == 0:
		if count > 1:
			print()
		print(">chr0_" + str(count))
		count += 1
	print(newseq[i], end="")
	print("N"*1000, end = "")
print()
