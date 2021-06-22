#!/usr/bin/python3

"""
  Find a region in a PAF file which is not aligned
"""

import sys

scaffolds = dict()

for i in open(sys.argv[1]):
    cols = i.rstrip().split("\t")
    if cols[0] not in scaffolds:
        scaffolds[cols[0]] = [0] * int(cols[1])
    for j in range(int(cols[2]), int(cols[3])):
        scaffolds[cols[0]][j] = 1

for i in scaffolds:
    start = 0
    for j in range(len(scaffolds[i])-1):
        if scaffolds[i][j] == 0 and scaffolds[i][j-1] == 1:
            start = j
        if scaffolds[i][j] == 1 and scaffolds[i][j-1] == 0:
            if j - start > 1000:
                print(i, start, j)
