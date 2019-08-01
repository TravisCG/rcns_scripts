#!/usr/bin/python3

import sys

ref = dict()

for i in sys.stdin:
	line = i.rstrip()
	fields = line.split("\t")
	if line.startswith('@SQ'):
		name = fields[1].replace('SN:', '')
		length = fields[2].replace('LN:', '')
		ref[name] = int(length)
	if not line.startswith('@'):
		if fields[2] == '*':
			continue
		name   = fields[2]
		start  = int(fields[3])
		length = ref[name]
		if start < 400 or start > length - 400:
			print(line)
	else:
		print(line)
