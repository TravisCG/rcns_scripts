#!/usr/bin/python3

import math
import sys

N = 250000.0 # This is very arbitary

peaks = open(sys.argv[1])
peaks.readline()
for i in open(sys.argv[1]):
    fields = i.rstrip().split()
    m      = float(fields[2])
    n      = float(fields[3])
    k      = float(fields[4])
    lambda_ = m * n / N
    exp(-lambda_)
