#!/usr/bin/python3

import sys

genes = list()

for i in open(sys.argv[1]):
    fields = i.rstrip().split("\t")
    genes.append(fields)

for i in open(sys.argv[2]):
    fields = i.rstrip().split("\t")
    found = list()
    for g in genes:
        if fields[0] == g[0] and int(fields[1]) < int(g[2]) and int(fields[2]) > int(g[1]):
            found.append(g[4])
    print(i.rstrip(),",".join(found), sep = "\t")

