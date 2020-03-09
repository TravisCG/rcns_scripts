#!/usr/bin/python

"""
   GI replace
   I have a lots of blast results. The downloaded database contains only
   accession numbers. This script replace accesion numbers with
   real descriptions
"""

import sys

acc = dict()

for i in open(sys.argv[1]):
	fields = i.rstrip().split("\t")
	acc[fields[0]] = fields[1]

for i in open(sys.argv[2]):
	if not i.startswith("#"):
		fields = i.rstrip().split("\t")
		fields[1] = acc[fields[1].split(".")[0]]
		print("\t".join(fields))
