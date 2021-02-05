#!/usr/bin/python3

import sys

stuff = dict()
for i in open(sys.argv[1]):
	fields = i.rstrip().split()
	if fields[0] not in stuff:
		stuff[fields[0]] = dict()
	if fields[1] in stuff[fields[0]]:
		sys.stderr.write("Problem:" + i)
	stuff[fields[0]][fields[1]] = fields[2:]

for i in open(sys.argv[2]):
	fields = i.rstrip().split()
	if fields[0] in stuff and fields[5] in stuff[fields[0]]:
		fields = fields + stuff[fields[0]][fields[5]]
	else:
		fields = fields + ["1.0", "1.0", "1.0", "1.0"]
	print("\t".join(fields))
