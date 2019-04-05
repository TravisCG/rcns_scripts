#!/usr/bin/python3

"""
  Find overlapping motif with a VCF file
  The motif came from summitdb
"""

import sys
import gzip

class Motif:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

def recsearch(pos, array, loindex, hiindex):
    if hiindex - loindex < 2:
        if pos > array[loindex].start and pos < array[loindex].end:
            return True
        elif pos > array[hiindex].start and pos < array[hiindex].end:
            return True
        return False
    midindex = int(loindex + (hiindex - loindex) / 2)
    if pos > array[loindex].start and pos < array[midindex].end:
        recsearch(pos, array, loindex, midindex)
    else:
        recsearch(pos, array, midindex, hiindex)

def overlap(pos, array):
    if pos < array[0].start or pos > array[-1].end:
        return False
    loindex = 0
    hiindex = len(array)
    return recsearch(pos, array, loindex, hiindex)

motifs = dict()

mfile = open(sys.argv[1])
mfile.readline()

for i in mfile:
    (motifname, chrom, start, end) = i.rstrip().split("\t")
    start = int(start)
    end = int(end)
    if chrom not in motifs:
        motifs[chrom] = list()
    m = Motif(motifname, start, end)
    motifs[chrom].append(m)

for m in motifs:
    motifs[m] = sorted(motifs[m], key = lambda x: x.start)

for i in gzip.open(sys.argv[2]):
    line = i.decode('utf-8').rstrip()
    if line.startswith("#"):
        print(line)
        continue
    (chrom, pos) = line.split("\t")[0:2]
    chrom = chrom.replace('chr', '')
    pos = int(pos)
    if chrom not in motifs:
        continue
    if overlap(pos, motifs[chrom]):
        print(line)
    else:
        print("No overlap", chrom, pos, file = sys.stderr)
