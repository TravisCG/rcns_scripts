#!/usr/bin/python3

"""
   Rename node label in .nexml file using a table
   Because the nexml is pretty, we do not use xml
   parsing library, so it won't work if the xml
   is obfuscated.
   Usage: nexmlrename.py treefile table >newtreefile
"""

import sys
import re

oldnamere = re.compile('label="([^"]+)"')

names = dict()
for i in open(sys.argv[2]):
    f = i.rstrip().split("\t")
    names[f[1]] = f[0]

for i in open(sys.argv[1]):
    if "#node" in i and "label" in i:
        match = oldnamere.search(i)
        if match:
            oldname = match.group(1)
            if oldname in names:
                newname = names[oldname]
                i = i.replace(oldname, newname)
    print(i.rstrip())
