#!/usr/bin/python3

import sys
idx = dict()
for i in open(sys.argv[1]):
    fields = i.rstrip().split("\t")
    idx[fields[5]] = fields[0]
    if fields[6] in idx:
        fields[6] = idx[fields[6]]
    if fields[7] in idx:
        fields[7] = idx[fields[7]]
    print("\t".join(fields))
