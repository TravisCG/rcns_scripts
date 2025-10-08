#!/usr/bin/python3

import sys

def calcLD(g, pg):
    l = len(g)
    firstgeno = g[0] # first genotype in the current position
    prevgeno = pg[0] # first genotype in the previous position
    pA = 0.0
    pB = 0.0
    pAB = 0.0
    for i in range(l):
        if g[i] == firstgeno:
            pA += 1.0
        if pg[i] == prevgeno:
            pB += 1.0
        if g[i] == firstgeno and pg[i] == prevgeno:
            pAB += 1.0

    pA = pA / float(l)
    pB = pB / float(l)
    pAB = pAB / float(l)
    LD = pAB - (pA * pB)
    return LD

chip = open(sys.argv[1])
chip.readline() # read header and forget
prev_genotypes = []
prev_chro = ''
for i in chip:
    cols = i.rstrip().split()
    chro = cols[0]
    pos  = cols[1]
    genotypes = cols[2:]

    if prev_chro != '' and prev_chro == chro:
        LD = calcLD(genotypes, prev_genotypes)
        if LD == 0.0:
            print(chro, pos, prev_pos, sep="\t")

    prev_genotypes = genotypes
    prev_chro = chro
    prev_pos = pos
