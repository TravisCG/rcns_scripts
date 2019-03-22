#!/usr/bin/python3

"""
  The first parameter is a list, where every line is a key which should be removed from a table
  The second parameter is a table itself. The script check all the columns for the
  discarded word
"""

import sys

blacklist = set()

for i in open(sys.argv[1]):
    blacklist.add(i.rstrip())

for i in open(sys.argv[2]):
    fields = i.rstrip().split("\t")
    for f in fields:
        if f in blacklist:
            break
    else:
        print(i.rstrip())
