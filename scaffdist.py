#!/usr/bin/python3

import sys

prev = 0
pchr = '0'
for i in open(sys.argv[1]):
    fields = i.rstrip().split("\t")
    if fields[1] != pchr:
        prev = 0
    dist   = int(fields[2]) - prev
    print(dist)
    prev = int(fields[3])
    pchr = fields[1]
