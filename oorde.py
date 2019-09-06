#!/usr/bin/python3

"""
   Try to find out the order using the existing rabbit genome
   The script use only the primary reads, because those has
   the most precise position
"""

import sys
import pysam

align = pysam.AlignmentFile(sys.argv[1], "rb")
scaffolds = dict()

for rec in align.fetch():
    if not rec.is_secondary and rec.reference_name is not None and not rec.is_supplementary:
        if rec.reference_name not in scaffolds:
            scaffolds[rec.reference_name] = list()
        scaffolds[rec.reference_name].append( (rec.query_name, rec.reference_name, str(rec.reference_start), str(rec.reference_end)) )
align.close()

for chrx in scaffolds:
    s = sorted(scaffolds[chrx], key = lambda x: int(x[2]))
    for i in s:
        print( "\t".join(i) )
