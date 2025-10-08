#!/usr/bin/python3

import sys

def printHeader(line):
    cols = line.split("\t")
    out = list()
    out.append(cols[0])
    out.append(cols[1])
    for i in range(9, len(cols)):
        out.append(cols[i])
    print("\t".join(out))

def processGT(field):
    index1 = 0
    index2 = 0
    gt = field.split(':')[0]
    if gt[0] == "1":
        index1 = 1
    if gt[2] == "1":
        index2 = 1
    return (index1, index2)

def processLine(line):
    outline = list()
    cols = line.split("\t")
    chrx = cols[0]
    pos  = cols[1]
    nucs = [cols[3], cols[4]]
    outline.append(chrx)
    outline.append(pos)
    for i in range(9, len(cols)):
        index = processGT(cols[i])
        gt = nucs[index[0]] + "/" + nucs[index[1]]
        outline.append(gt)
    print("\t".join(outline))

for i in open(sys.argv[1]):
    if i.startswith("##"):
        continue
    elif i.startswith("#C"):
        printHeader(i.rstrip())
    else:
        processLine(i.rstrip())
