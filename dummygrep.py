#!/usr/bin/python3

"""
   This script represents if a user couldn't know
   how to manage a program always could write a
   script to overcome this.

   I have no idea how to run a blast search to find
   only the top result, so this script filter the
   tabular blast output to save it to me.
"""

import sys

filtered = dict()

for i in open(sys.argv[1]):
	if i.startswith("#"):
		continue
	f = i.rstrip().split("\t")
	if f[0] not in filtered:
		filtered[f[0]] = i.rstrip()

for i in filtered:
	print(filtered[i])
