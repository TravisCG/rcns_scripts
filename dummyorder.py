#!/usr/bin/python3

import sys

print("taxon\ttissue\tgroup\tvalue")

for i in open(sys.argv[1]):
    fields = i.rstrip().split("\t")
    if (fields[1] == "G1" or fields[1] == "G3"):
        taxon = fields[0]
        groups = fields
    else:
        tissue = fields[0]
        for j in range(1,4):
            print(taxon, tissue, groups[j], fields[j], sep = "\t")
