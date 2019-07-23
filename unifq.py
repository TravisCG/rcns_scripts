#!/usr/bin/python3

"""
   Read a FASTQ file and remove redundancy
   For example when the base calling has some bugs
   I hope you have enough RAM
"""

import sys

fastq = dict()

linenum = 0
for i in open(sys.argv[1]):
    if linenum % 4 == 0:
        readid = i.rstrip()
        fastq[readid] = list()
    fastq[readid].append(i.rstrip())
    linenum += 1

for i in fastq:
    print("\n".join(fastq[i]))
