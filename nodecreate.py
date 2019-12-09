#!/usr/bin/python3

"""
  Create Cytoscape-like hierarchy file form some
  inproper input
"""

import sys

for i in open(sys.argv[1]):
    fields = i.rstrip().split("\t")
    if len(fields) < 2:
        continue
    idx = fields[0]
    for j in fields[1].split(","):
        if j != "":
            print("%s\t%s" % (idx, j))
