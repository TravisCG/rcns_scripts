#!/usr/bin/python3

"""
   Read VCF file, creates MAF file for SignatureAnalyzer
"""

import gzip
import sys

def revcomp(txt):
    tr = str.maketrans('ATGC', 'TACG')
    return(txt[::-1].translate(tr))

ref = dict()
for i in open(sys.argv[2]):
    if i.startswith(">"):
        ids = i.rstrip().split()[0][1:]
        ref[ids] = list()
    else:
        ref[ids].append(i.rstrip())

for i in ref:
    ref[i] = "".join(ref[i])

for i in gzip.open(sys.argv[1]):
    line = i.decode('utf-8').rstrip()
    if line.startswith('##'):
        continue
    fields = line.split("\t")
    if fields[0] == '#CHROM':
        samples = fields[9:]
    else:
        refa = fields[3]
        alta = fields[4]
        pos  = int(fields[1])
        chrx = fields[0]

        if len(refa) != 1 or len(alta) != 1 or alta == '*':
            continue
        index   = 0
        context = ref[chrx][pos-2:pos+1]
        if refa != 'A' and refa != 'C':
            refa = revcomp(refa)
            alta = revcomp(alta)
            context = revcomp(context)
        for s in fields[9:]:
            if '1' in s.split(':')[0]:
                print(samples[index], 'SNP', refa, alta, context, sep = '\t')
            index += 1
