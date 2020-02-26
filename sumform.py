#!/usr/bin/python

"""
   Reads a concatenated XML file (get by esummary)
   and produce a two columns table
"""

import sys
import re

tag = re.compile('<[^>]+>')

for i in open(sys.argv[1]):
	if 'Caption' in i:
		caption = tag.sub("", i.strip())
	if 'Title' in i:
		title = tag.sub("", i.strip())
		print(caption, title, sep = "\t")
