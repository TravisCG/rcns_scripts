#!/usr/bin/python3

import sys
import re

nodelenre = re.compile("length_(\d+)_")
full = set()
every = set()
for i in open(sys.argv[1]):
    cols = i.rstrip().split()
    match = nodelenre.search(cols[0])
    if match:
        nodelen = float(match.group(1))
        if nodelen < 3000:
            continue
        every.add(cols[0])
        dist = float(cols[2]) - float(cols[1])
        if dist / nodelen > 0.80 or (float(cols[1]) / nodelen < 0.2 and float(cols[2]) / nodelen > 0.75):
            full.add(cols[0])
    else:
        print("Problem, there is no length information in the contig name")
        break

for i in every - full:
    print(i)
