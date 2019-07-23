#!/usr/bin/python3

import sys

f = open(sys.argv[1])
f.readline()

for i in f:
    posstr = i.rstrip().split("\t")[0]
    start, end = posstr.split("_")[1:3]
    print(int(end) - int(start))
f.close()
