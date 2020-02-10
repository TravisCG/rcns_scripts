#!/usr/bin/python3

import sys
import glob
import re

ccpatt = re.compile("(\D+)([0-9.]+)\.([23]d)")

path2gene = dict()
pathfile = open(sys.argv[1])
pathfile.readline()
for i in pathfile:
    fields = i.rstrip().split(',')
    if fields[2] not in path2gene:
        path2gene[fields[2]] = list()
    path2gene[fields[2]].append(fields[0])
pathfile.close()

genes = dict()
count = 0
head1 = list()
head2 = list()
head3 = list()
head3.append("Pathway")
for p in path2gene:
    for i in path2gene[p]:
        genes[i] = count
        count += 1
        head1.append(p)
        head2.append(i)
        head3.append("Pathway")

print(",,,", ",".join(head1),"DEG", sep = ",")
print(",,,", ",".join(head3), sep = ",")
print("row_order,chemical_name,chemical_source_sid,celltype", ",".join(head2),"DEG", sep = ",")

files = glob.glob("foldchange/*")
rowcount = 1
for f in files:
    condname = f.split('/')[-1].replace(".tsv", "")
    match = ccpatt.search(condname)
    if match:
        chem = match.group(1)
        cc   = match.group(2)
        cell = match.group(3)
    else:
        print("regular expression is not good")
        exit(0)
    outrow = ['0'] * (count + 5)
    outrow[0] = str(rowcount)
    outrow[2] = chem
    outrow[3] = chem + "_" + cc
    outrow[1] = cell
    inp = open(f)
    inp.readline()
    DEG = 0
    for line in inp:
        fields = line.rstrip().split("\t")
        gene   = fields[0]
        if gene not in genes:
            continue
        lfc    = fields[2]
        outrow[genes[gene] + 4] = lfc
        pval   = float(fields[6])
        if pval < 0.05:
            DEG += 1
    inp.close()
    outrow[-1] = str(DEG)
    print(",".join(outrow))
    rowcount += 1
