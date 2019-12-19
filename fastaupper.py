#!/usr/bin/python3

import sys

for i in open(sys.argv[1]):
	if i.startswith(">"):
		print(i.rstrip())
	else:
		print(i.rstrip().upper())
