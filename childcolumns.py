#!/usr/bin/python3

import sys

same = dict()
for i in open(sys.argv[2]):
    fields = i.rstrip().split()
    if fields[0] not in same:
        same[fields[0]] = set()
    same[fields[0]].add(fields[1])

for i in open(sys.argv[1]):
    fields = i.rstrip().split("\t")
    geneid = fields[0]
    if geneid not in same:
        fields = fields + ["unknown"] * 8
    else:
        for child in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            if child in same[geneid]:
                fields.append("same")
            else:
                fields.append("diff")
    print("\t".join(fields))
