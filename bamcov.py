#!/usr/bin/python3

import pysam
import sys

def printhelp():
    print("BAM nucleotide composition in specified positions")
    print("Usage:")
    print("bamcov.py -bam input.bam -pos chr:pos")
    print("or")
    print("bamcov.py -bam input.bam -posfile positions.txt\n")
    print("-bam: input bam file. Sorted, indexed")
    print("-pos: one position in the following format: contig:position")
    print("-posfile: multiple positions in a file")
    sys.exit(0)

pfname = ""

for i in range(1, len(sys.argv)):
    if sys.argv[i] == "-h":
        printhelp()
    if sys.argv[i] == "-bam":
        bamname = sys.argv[i+1]
    if sys.argv[i] == "-posfile":
        pfname = sys.argv[i+1]
    if sys.argv[i] == "-pos":
        pos = sys.argv[i+1]

positions = list()
if pfname != "":
    try:
        f = open(pfname)
    except(FileNotFoundError):
        print("Opening position file is failed!", file=sys.stderr)
        sys.exit(1)
    for i in f:
        positions.append(i.rstrip())
    f.close()
else:
    positions.append(pos)

try:
    bam = pysam.AlignmentFile(bamname, "rb")
except(FileNotFoundError):
    print("Bam file not found", file = sys.stderr)
    sys.exit(1)

print("pos\tA\tT\tG\tC\tdel")
for pos in positions:
    chrx, choord = pos.split(":")
    choord = int(choord) - 1
    try:
        count = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'del': 0}
        reads = bam.fetch(chrx, choord, choord+1)
        for seq in reads:
            for block in seq.get_aligned_pairs():
                if block[1] == choord:
                    if block[0]:
                        count[seq.query_sequence[block[0]]] += 1
                    else:
                        count['del'] += 1
        print(pos, count['A'], count['T'], count['G'], count['C'], count['del'], sep = "\t")
    except(ValueError):
        print("Invalid contig:", chrx, file = sys.stderr)
        continue
