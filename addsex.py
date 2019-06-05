#!/usr/bin/python3

import sys

sex = dict()
for i in open(sys.argv[1]):
    fields = i.rstrip().split("\t")
    if len(fields) > 1:
        sex[fields[0]] = fields[1]

sec = open(sys.argv[2])
print(sec.readline().rstrip() + "\tsex")
for i in sec:
    fields = i.rstrip().split("\t")
    if fields[2] in sex:
        fields.append(sex[fields[2]])
    else:
        fields.append('0')
    print("\t".join(fields))
