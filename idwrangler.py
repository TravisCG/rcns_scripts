#!/usr/bin/python

import sys

shtfile = open(sys.argv[1])
shtfile.readline()
tatto2wgs = dict()
parents = set()
for i in shtfile:
	fields = i.split("\t")
	if fields[0] not in tatto2wgs:
		tatto2wgs[fields[0]] = list()
	else:
		print(fields[0], "fuck", file=sys.stderr)
	tatto2wgs[fields[0]] = [fields[1], fields[2], fields[3].rstrip()]
	parents.add(fields[2])
	parents.add(fields[3].rstrip())

for i in tatto2wgs:
	rec = tatto2wgs[i]
	wgsid = rec[0]
	father = rec[1]
	mother = rec[2]
	if father in tatto2wgs and mother in tatto2wgs:
		print(wgsid, tatto2wgs[father][0], tatto2wgs[mother][0])

for i in parents:
	if i in tatto2wgs:
		print(tatto2wgs[i][0],0,0)
