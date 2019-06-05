#!/usr/bin/python3

import sys

f = open(sys.argv[1])
header = f.readline().rstrip()
print(header)
prevend = 0

for line in f:
    chrom, start, end, samples = line.rstrip().split("\t",3)
    start = int(start)
    end   = int(end)
    if start - prevend == 1 and samples == prevsamples:
        # merge
        pass
    else:
        if prevend != 0:
            print(prevchr, mergestart, prevend, prevsamples, sep = "\t")
        mergestart = start
    prevend = end
    prevsamples = samples
    prevchr = chrom
print(chrom, mergestart, prevend, prevsamples, sep = "\t")
