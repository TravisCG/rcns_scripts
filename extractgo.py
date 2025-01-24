#!/usr/bin/python3

import sys

f = open(sys.argv[1])
f.readline()
for i in f:
	fields = i.rstrip().split("\t")
	intron = fields[1]
	allgo  = ""
	xgo    = fields[12]
	if xgo != ".":
		allgo += "`" + xgo
	pgo    = fields[13]
	if pgo != ".":
		allgo += "`" + pgo
	ugo    = fields[14]
	if ugo != ".":
		allgo += "`" + ugo
	pieces = allgo.split("`")[1:]
	for p in pieces:
		terms = p.split("^")
		print(intron, terms[0], terms[2], sep = "\t")
