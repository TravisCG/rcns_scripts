#!/usr/bin/python3

import sys

ids = dict()

for i in open(sys.argv[1]):
	c = i.rstrip().split()
	ids[c[1]] = c[0]

for i in open(sys.argv[2]):
	l = i.rstrip()
	if l[1:len(l)] in ids:
		print(">" + ids[l[1:len(l)]])
	else:
		print(l)
