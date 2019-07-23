#!/usr/bin/python3

"""
  Alignment statistics with reference name
  prefix.
"""

import pysam
import sys

def calcMismatch(read, all_refs):
    mismatch = 0
    ab = read.get_aligned_pairs()
    reference = all_refs[read.reference_name]
    for i in ab:
        if i is None:
            continue
        if i[0] is not None and i[1] is not None:
            query_base = read.query_sequence[i[0]]
            ref_base = reference[i[1]]
            if query_base != ref_base:
                mismatch += 1
    return(mismatch)

def calcIndel(read, all_refs):
    ct = read.cigartuples
    indelcount = 0
    reference = all_refs[read.reference_name]
    for i in ct:
        if i[0] == 1 or i[0] == 2:
            indelcount += i[1]
    return(indelcount)

align = pysam.AlignmentFile(sys.argv[1], "rb")
reads = align.fetch(until_eof = True)

# Read reference sequence for mismatch identification
reffile = open(sys.argv[2])
refseq = dict()
for i in reffile:
    if i.startswith(">"):
        seqname = i[1:].split()[0]
        refseq[seqname] = list()
        continue
    refseq[seqname].append(i.rstrip())
reffile.close()
for i in refseq:
    refseq[i] = "".join(refseq[i])

# Print header
print("mapped\taligned_len\tmismatchnum\tindelnum\traw_read_len\treference_prefix")

# Parsing reads
for i in reads:
    output = []
    #alignment_len = i.reference_end - i.reference_start
    if i.is_secondary or i.is_supplementary:
        continue
    if i.is_unmapped:
        mapped = "0"
        mismatchnum = 0
        indelnum = 0
    else:
        mapped = "1"
        mismatchnum = calcMismatch(i, refseq)
        indelnum = calcIndel(i, refseq)

    output.append(i.query_name)
    output.append(mapped)
    #output.append(str(alignment_len))
    output.append(str(i.query_alignment_length))
    output.append(str(mismatchnum))
    output.append(str(indelnum))
    output.append(str(i.query_length))
    if i.reference_name != None:
        output.append(i.reference_name.split("_")[0])
    else:
        output.append("*")

    print("\t".join(output))
