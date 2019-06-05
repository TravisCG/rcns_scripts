#!/usr/bin/python3

import sys

rabbit = dict()
for i in open(sys.argv[1]):
    fields = i.rstrip().split("\t")
    rabbit[fields[0]] = (fields[2], fields[4])

for i in open(sys.argv[2]):
    fields = i.rstrip().split("\t")
    if fields[6] in rabbit:
        fields.append(rabbit[fields[6]][0])
        fields.append(rabbit[fields[6]][1])
    else:
        fields.append("0")
        fields.append("0")
    print("\t".join(fields))
