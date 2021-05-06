#!/usr/bin/python3

import sys

col1 = sys.argv[1]
fn   = sys.argv[2]

for i in open(fn):
    fields = i.rstrip().split("\t")
    if col1 in fields[1] and "Bacteria" not in fields[2]:
        print(i.rstrip())
