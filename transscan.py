#!/usr/bin/python3

"""
   Finding translocation or recombination in our annominer's output
"""

import sys

storage = dict()

for i in sys.argv[1:]:
    f = open(i)
    for j in f:
        cols       = j.rstrip().split()
        scaffold   = cols[0]
        start      = int(cols[1])
        stop       = int(cols[2])
        chromosome = cols[3]

        if stop - start < 2:
            continue
        if scaffold not in storage:
            storage[scaffold] = dict()
        if chromosome not in storage[scaffold]:
            storage[scaffold][chromosome] = list()
        storage[scaffold][chromosome].append([start, stop])
    f.close()

for scaffold in storage:
    chromosomes = list(storage[scaffold].keys())
    for k in range(len(chromosomes)-1):
        for l in range(k+1,len(chromosomes)):
            chrom1 = chromosomes[k]
            chrom2 = chromosomes[l]
            overlap = False
            for i in range(len(storage[scaffold][chrom1])):
                for j in range(len(storage[scaffold][chrom2])):
                    start1 = storage[scaffold][chrom1][i][0]
                    stop1  = storage[scaffold][chrom1][i][1]
                    start2 = storage[scaffold][chrom2][j][0]
                    stop2  = storage[scaffold][chrom2][j][1]
                    if stop1 > start2 and start1 < stop2:
                        overlap = True
                        break
                if overlap == True:
                    break
            if not overlap:
                print(scaffold, chrom1, chrom2)
