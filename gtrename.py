#!/usr/bin/python3

"""
   Guide tree sequence renamer
   Mauve creates a guide tree, but
   the names are just seq1...seqN
   This script renames it using
   the log file
"""

import sys
import re

seqnames = list()
target   = re.compile("seq(\d+)")

for i in open(sys.argv[1]):
    if i.startswith('>'):
        break
    if "base pairs" in i:
        filename = " ".join(i.rstrip().split()[:-3])
        seqnames.append(filename)

for i in open(sys.argv[2]):
    tokens = i.rstrip().split(":")
    out = list()
    for t in tokens:
        m = target.search(t)
        if m:
            index = int(m.group(1)) - 1
            newname = seqnames[index].replace(".fasta", "")
            oldname = m.group(0)
            out.append(t.replace(oldname, newname))
        else:
            out.append(t)
    print(":".join(out))
