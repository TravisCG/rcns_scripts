#!/usr/bin/python3

"""
   Overlap with summitdb
"""

import sys

summit = set()
for i in open(sys.argv[1]):
    idx = i.split("\t")[8]
    summit.add(idx)

f = open(sys.argv[2])
print(f.readline().rstrip(),"overlapwithsummit",sep="\t")
for i in f:
    idx = i.split("\t")[2]
    if idx in summit:
        summitcolumn = "yes"
    else:
        summitcolumn = "no"
    print(i[:-1], summitcolumn, sep = "\t")
