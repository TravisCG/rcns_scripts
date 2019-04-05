#!/usr/bin/python3

import sys
import gzip
import re

for i in gzip.open(sys.argv[1]):
    line = i.decode('utf-8').rstrip()
    if line.startswith("##"):
        print(line)
        continue
    fields = line.split("\t")
    chrom = fields[0]
    pos = fields[1]
    rsid = fields[2]
    if line.startswith("#"):
        print(line)
        continue
    gts = list()
    for i in range(9, len(fields)):
        gt = fields[i].split(":")[0]
        a,b = re.split("[/|]", gt)
        if a == '.':
            a = '0'
        if b == '.':
            b = '0'
        a = int(a)
        b = int(b)
        if a + b == 0:
            gts.append(0)
        else:
            gts.append(1)
    if sum(gts) == 1 and gts[16] == 1:
        print(line)
