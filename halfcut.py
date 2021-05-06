#!/usr/bin/python3

import sys
correlations = dict()
infile = open(sys.argv[1])
infile.readline()
for i in infile:
    cols = i.rstrip().split("\t")
    if cols[1] == cols[2]:
        continue
    if cols[1] not in correlations:
        correlations[cols[1]] = dict()
    if cols[2] in correlations and cols[1] in correlations[cols[2]]:
        continue
    if float(cols[3]) > 0.0:
        continue
    correlations[cols[1]][cols[2]] = i.rstrip()

for cond1 in correlations:
    for cond2 in correlations[cond1]:
        print(correlations[cond1][cond2])
