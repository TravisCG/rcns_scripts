#!/usr/bin/python3

"""
   Read scaffold positions in genome
   Read sequencing read positions in scaffolds (both forward and reverse)
   Finally try to find out which scaffolds are close to each other
"""

import sys

class Bridge:
    def __init__(self):
        self.name = ""
        self.readsfromA = set()
        self.readsfromB = set()

bridges = dict()

for j in range(1,3):
    for i in open(sys.argv[j]):
        fields = i.rstrip().split()
        if fields[0] not in bridges:
            bridges[fields[0]] = list()
        bridges[fields[0]].append(fields[1])

counter = dict()
for i in bridges:
    if len(bridges[i]) == 2:
        scaffolds = "_".join(sorted(bridges[i]))
        if scaffolds not in counter:
            counter[scaffolds] = 0
        counter[scaffolds] += 1

for sc in counter:
    print(sc, counter[sc])
