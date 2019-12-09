#!/usr/bin/python3

"""
   This script converts the table downloaded from Panther.org
   to a Cytoscape compatible table. The script needs two tables.
   The first one is the result, the second one is the hierarchy in
   node_id\tparent_id format. If a node has more than one parents,
   you need to create as many rows as many parents the row have.
"""

import sys

def walkup(idx, hierarchy, steps, sig):
    if idx not in hierarchy:
        return
    parents = hierarchy[idx]
    for p in parents:
        k = idx + "\t" + p
        if k not in steps:
            steps[k] = sig
        walkup(p, hierarchy, steps, "0")

hier  = dict()
steps = dict()

for i in open(sys.argv[2]):
    fields = i.rstrip().split("\t")
    if fields[0] not in hier:
        hier[fields[0]] = list()
    hier[fields[0]].append(fields[1])

for column in [2,3,4,5,6]:
    ontofile = open(sys.argv[1])
    header = ontofile.readline().rstrip().split("\t")
    for i in ontofile:
        fields = i.rstrip().split("\t")
        idx = fields[1]
        sig = fields[column] # change this according to which column you need
        if sig == 'ns':
            continue
        walkup(idx, hier, steps, sig)
    ontofile.close()

    out = open(header[column-1], "w")
    out.write("source\tdestination\tsignif\n")
    for s in steps:
        out.write(s + "\t" + steps[s] + "\n")
    out.close()
