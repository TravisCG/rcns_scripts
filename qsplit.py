#!/usr/bin/python3

import sys

count = 0
j = 1
out = open("chunk." + str(j) + ".fasta", "w")
for i in open(sys.argv[1]):
	if i.startswith('>'):
		count += 1
		if (count % 800) == 0:
			j += 1
			out.close()
			out = open("chunk." + str(j) + ".fasta", "w")
	out.write(i)
