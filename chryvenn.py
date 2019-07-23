#!/usr/bin/python3

import sys

def printbivar(fields, gts, allele):
    print(fields[0], fields[1], fields[2], gts[allele], sep ="\t", end = "\t")
    gt = list()
    for i in fields[4:]:
        if i[2] == str(allele):
            gt.append('1')
        else:
            gt.append('0')
    print("\t".join(gt))

f = open(sys.argv[1])
print(f.readline().rstrip())

for i in f:
    fields = i.rstrip().split("\t")
    gts    = [fields[2]] + fields[3].split(",")
    alleles = set()
    for j in fields[4:]:
        a = j[0]
        b = j[2]
        if a == '.':
            a = '0'
        if b == '.':
            b = '0'
        alleles.add(int(a))
        alleles.add(int(b))
    alleles = sorted(list(alleles))
    if len(alleles) > 2:
        #FIXME if the genotype is something like 1/2, 2/3, etc, the output will be strange
        for j in alleles[1:]:
            printbivar(fields, gts, j)
    else:
        printbivar(fields, gts, alleles[-1])
