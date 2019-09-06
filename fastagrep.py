#!/usr/bin/python3

import sys

fasta = dict()

for i in open(sys.argv[1]):
    if i.startswith(">"):
        idx = i.rstrip().split()[0][1:]
        fasta[idx] = list()
    else:
        fasta[idx].append(i.rstrip())

for i in open(sys.argv[2]):
    idx = i.rstrip()
    if idx in fasta:
        print(">%s" % idx)
        print("".join(fasta[idx]))
