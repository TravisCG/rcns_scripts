#!/usr/bin/python3

"""
   Get full length scaffolds and chromosomes
"""

import sys
import re

nodelenre = re.compile("length_(\d+)_")

for i in open(sys.argv[1]):
    cols = i.rstrip().split()
    match = nodelenre.search(cols[0])
    if match:
        nodelen = float(match.group(1))
        if nodelen < 3000:
            continue
        dist = float(cols[2]) - float(cols[1])
        if dist / nodelen > 0.90 or (float(cols[1]) / nodelen < 0.05 and float(cols[2]) / nodelen > 0.95):
            print(i.rstrip())
    else:
        print("Problem, there is no length information in the contig name")
        break
