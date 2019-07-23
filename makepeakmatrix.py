#!/usr/bin/python3

import sys
import bz2

def newfounder(founder, values, experiment, pvalue, chrom, start, end, all_exp):
    founder[0] = chrom
    founder[1] = start
    founder[2] = end
    values = ['0'] * len(all_exp)
    col_exp = all_exp[experiment]
    values[col_exp] = pvalue

def printvalues(founder, values):
    print("%s_%d_%d\t%s" % (founder[0], founder[1], founder[2], "\t".join(values)))

exp = open(sys.argv[2])
exp.readline()
count = 0
all_exp = dict()
header = list()
for i in exp:
    fields = i.rstrip().split("\t")
    all_exp[fields[0]] = count
    header.append(fields[0])
    count += 1

compressed = bz2.open(sys.argv[1])
compressed.readline()

founder = ['', 0, 0]
values = ['0'] * len(all_exp)
print("\t".join(header))

for i in compressed:
    line = i.decode('utf-8').rstrip()
    (experiment, pvalue, chrom, start, end) = line.split("\t")
    start = int(start)
    end = int(end)
    if float(pvalue) < 0.05:
        pvalue = '1'
    else:
        pvalue = '0'
    if founder[0] != chrom:
        if founder[0] != '':
            printvalues(founder, values)
        newfounder(founder, values, experiment, pvalue, chrom, start, end, all_exp)
        continue
    else:
        if founder[2] > start:
            founder[2] = end
            col_exp = all_exp[experiment]
            values[col_exp] = pvalue
        else:
            printvalues(founder, values)
            newfounder(founder, values, experiment, pvalue, chrom, start, end, all_exp)
printvalues(founder, values)
