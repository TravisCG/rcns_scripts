#!/usr/bin/python3

"""
  We have several GO results. This script creates one table with several columns
"""

import sys

class GO:
    def __init__(self, name):
        self.name = name
        self.treatments = dict()

finaltable = dict()
finalheader = list()
finalheader.append("goterm")
finalheader.append("godesc")
for i in sys.argv[1:]:
    f = open(i)
    header = f.readline().rstrip().split("\t")
    finalheader.extend(header[1:])
    for line in f:
        fields = line.rstrip().split("\t")
        goterm = fields[1]
        if goterm not in finaltable:
            finaltable[goterm] = GO(fields[0])
        for j in range(2, len(fields)):
            trname = header[j-1]
            if fields[j] != "ns":
                try:
                    finaltable[goterm].treatments[trname] = float(fields[j])
                except ValueError:
                    finaltable[goterm].treatments[trname] = float(fields[j][3:])
    f.close()

print("\t".join(finalheader))
for goterm in finaltable:
    out = list()
    out.append(goterm)
    out.append(finaltable[goterm].name)
    for trname in finalheader[2:]:
        if trname not in finaltable[goterm].treatments:
            out.append('0')
        else:
            out.append(str(finaltable[goterm].treatments[trname]))
    print("\t".join(out))
