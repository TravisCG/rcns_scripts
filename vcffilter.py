#!/usr/bin/python3

import sys

markerpos = set()

for i in open(sys.argv[1]):
	if i.startswith("#"):
		continue
	fields = i.rstrip().split()
	markerpos.add("%s_%s_%s_%s" % (fields[0], fields[1], fields[3], fields[4]))

for i in sys.stdin:
	if i.startswith("#"):
		print(i.rstrip())
		continue
	fields = i.split("\t")
	alts = fields[4].split(",")
	for a in alts:
		pos = "%s_%s_%s_%s" % (fields[0], fields[1], fields[3], a)
		if pos in markerpos:
			print(i.rstrip())
			break
