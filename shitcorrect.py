#!/usr/bin/python3

"""
I get a shit called Excel table
This script try to fix the crappy header names, sample ids and so on
"""

import sys

shitfile = open(sys.argv[1])
shitfile.readline() # skip stupid header
realheader = shitfile.readline().rstrip().split("\t")
treatments = [""] * len(realheader)
sample     = [""] * len(realheader)


for i in range(len(realheader)):
    shitentry = realheader[i]
    if shitentry.endswith("i"):
        treatments[i] = "ileum"
        sample[i] = shitentry[:-1]
    elif shitentry.endswith("j"):
        treatments[i] = "jejunum"
        sample[i] = shitentry[:-1]
    elif shitentry.endswith("d"):
        treatments[i] = "duodenum"
        sample[i] = shitentry[:-1]
    elif shitentry.startswith("F0"):
        treatments[i] = "faces_0"
        sample[i] = shitentry[2:]
    elif shitentry.startswith("F21"):
        treatments[i] = "faces_21"
        sample[i] = shitentry[3:]
    else:
        treatments[i] = "more shit"
        sample[i] = "just shit"

output = dict()
columns = set()

for line in shitfile:
    fields = line.rstrip().split("\t")
    otu = fields[0]
    for i in range(1,len(fields)):
        coltype = "%s_%s" % (treatments[i], otu)
        columns.add(coltype)
        if sample[i] not in output:
            output[sample[i]] = dict()
        output[sample[i]][coltype] = fields[i]

columns = list(columns)

okfile = open(sys.argv[2])
print(okfile.readline().rstrip(), "\t".join(columns), sep = "\t")
for i in okfile:
    sampleid = i.split("\t")[0]
    outline = list()
    for j in columns:
        outline.append(output[sampleid][j])
    print(i.rstrip(), "\t".join(outline), sep = "\t")
