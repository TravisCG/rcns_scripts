#!/usr/bin/python3

import sys
import re

"""
   Read two Saccharomyces annotation and try
   to find colinear parts. We would like to
   identify common regions.
"""

def gffread(filename):
    protnamere = re.compile("([^|]+_YEAST);")
    lengthere = re.compile("length_(\d+)_")
    order = dict()
    f = open(filename)
    for i in f:
        if "YEAST" not in i:
            continue
        columns = i.rstrip().split()
        if columns[1] != "blastx":
            continue
        if columns[2] != "protein_match":
            continue
        match = lengthere.search(columns[0])
        if match:
            length = int(match.group(1))
            if length < 3000:
                continue
        match = protnamere.search(columns[8])
        if match:
            if columns[0] not in order:
                order[columns[0]] = list()
            order[columns[0]].append([match.group(1), columns[3]])
    f.close()
    return order

strain1 = gffread(sys.argv[1])
strain2 = gffread(sys.argv[2])

for contig1 in strain1:
    col = len(strain1[contig1])

    for contig2 in strain2:
        row = len(strain2[contig2])
        table = list()
        for i in range(row):
            newrow = [0] * col
            table.append(newrow)

        for x in range(col):
            genename1, pos1 = strain1[contig1][x]
            for y in range(row):
                genename2, pos2 = strain2[contig2][y]
                if genename1 == genename2:
                    table[y][x] = 1

        for x in range(col):
            for y in range(row):
                if table[y][x] == 1:
                    run = True
                    step = 0
                    while run:
                        if table[y + step][x - step] == 1:
                            table[y + step][x - step] = 0
                        step += 1
                        if y + step == row or x + step == col:
                            run = False
                    print(contig1, strain1[contig1][x][1], strain1[contig1][x + step - 1][1], contig2, strain2[contig2][y][1], strain2[contig2][y + step - 1][1], step - 1)
