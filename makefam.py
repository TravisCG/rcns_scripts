#!/usr/bin/python3

import sys

rabbit = dict()

for i in open(sys.argv[1]):
    fields = i.rstrip().split()
    rabbit[fields[0]] = fields[1]

for i in open(sys.argv[2]):
    fields = i.rstrip().split()
    if rabbit[fields[0]] == 'sensitive':
        fields[5] = '0'
    else:
        fields[5] = '1'
    print("\t".join(fields))
