#!/usr/bin/python3

"""
   Remove duplicated files.
   First, need a find command with your favourite
   checksum calculator (sha256, sha512)
   and a sort | uniq -c
"""

import gzip
import sys
import os

blackhash = dict()
for i in open(sys.argv[1]):
	entry = i.rstrip().split()[1]
	blackhash[entry] = 0

for i in gzip.open(sys.argv[2]):
	text = i.decode('UTF-8').rstrip()
	cols = text.split("  ")
	md5 = cols[0]
	path = "  ".join(cols[1:])
	if md5 in blackhash:
		if blackhash[md5] > 0:
			try:
				os.remove(path)
			except OSError:
				print("Cannot remove ", path)
		blackhash[md5] += 1
