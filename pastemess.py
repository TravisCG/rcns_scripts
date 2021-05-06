#!/usr/bin/python3

import sys

def reader(filename, d):
    f = open(filename)
    f.readline()
    for i in f:
            fields = i.rstrip().split("\t")
            d[fields[0]] = fields[1:]

def predireader(filename, d):
    for i in open(filename):
        fields = i.rstrip().split(" ")
        child  = int(fields[1])
        if fields[0] not in d:
            d[fields[0]] = dict()
        d[fields[0]][child] = fields[2]

predi = dict()
predinocomb = dict()
logfc = dict()
padj = dict()
same = dict()
samenocomb = dict()

reader(sys.argv[1], predi)
reader(sys.argv[2], predinocomb)
reader(sys.argv[3], logfc)
reader(sys.argv[4], padj)
predireader(sys.argv[5], same)
predireader(sys.argv[6], samenocomb)

print("geneid\tn_parental_geno\tn_parental_geno_nocomb\tp_het\tp_het_nocomb\tp_het_hom\tp_het_hom_nocomb\tp_hom\tp_hom_nocomb\tdecision\tdecision_nocomb",end="")
for i in range(1,9):
    print("\tchild%d_logFC" % (i), end = "")
    print("\tchild%d_padj" % (i), end = "")
    print("\tchild%d_pred" % (i), end = "")
    print("\tchild%d_pred_nocomb" % (i), end = "")

print("\tfather_logFC\tfather_padj")

for geneid in predi:
    output = list()
    output.append(geneid)
    for j in range(0,5):
        output.append(predi[geneid][j])
        output.append(predinocomb[geneid][j])
    for j in range(1,9):
        output.append(logfc[geneid][j])
        output.append(padj[geneid][j-1])
        if geneid in same and j in same[geneid]:
            output.append("same")
        else:
            output.append("diff")
        if geneid in samenocomb and j in samenocomb[geneid]:
            output.append("same")
        else:
            output.append("diff")
    output.append(logfc[geneid][9])
    output.append(padj[geneid][8])
    print("\t".join(output))
