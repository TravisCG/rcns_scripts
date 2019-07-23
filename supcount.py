#!/usr/bin/python3

"""
   This script reads a BAM file, create 1000 bp long bins
   and calculate the percentage of supplementary reads.
   Working only with one reference sequence and count
   only, when the read starts on the bin.
"""

import sys
import pysam

align = pysam.AlignmentFile(sys.argv[1], "rb")
reads = align.fetch(until_eof = True)
bins  = list()
refl  = int(align.get_reference_length(align.get_reference_name(0)) / 1000) + 1
for i in range(refl):
    bins.append([0,0])

for r in reads:
    if r.is_unmapped:
        continue
    binpos = int(r.reference_start / 1000)
    if r.is_supplementary:
        bins[binpos][0] += 1
    bins[binpos][1] += 1

for i in range(refl):
    if bins[i][1] == 0:
        print("0.0")
    else:
        print(bins[i][0] / bins[i][1])
