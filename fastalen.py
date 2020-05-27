#!/usr/bin/python3

import sys

seq = ""
for i in open(sys.argv[1]):
	if i.startswith('>'):
		if seq != "":
			print(idx,len(seq))
		idx = i.rstrip()[1:]
		seq = ""
	else:
		seq = seq + i.rstrip()
print(idx,len(seq))
