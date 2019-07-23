#!/usr/bin/python3

import sys

f = open(sys.argv[1])
f.readline()

for i in f:
    values = i.rstrip().split("\t")[1:]
    values = [int(x) for x in values]
    print(sum(values))
f.close()
