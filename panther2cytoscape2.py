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
        nosig = [" "] + ['0'] * (len(sig) - 1)
        walkup(p, hierarchy, steps, nosig)

hier  = dict()
steps = dict()

for i in open(sys.argv[2]):
    fields = i.rstrip().split("\t")
    if fields[0] not in hier:
        hier[fields[0]] = list()
    hier[fields[0]].append(fields[1])

ontofile = open(sys.argv[1])
header = ontofile.readline().rstrip().split("\t")
header.insert(1, "goparent")
for i in ontofile:
    fields = i.rstrip().split("\t")
    idx = fields[0]
    #sig = "\t".join(fields[1:])
    sig = fields[1:]
    walkup(idx, hier, steps, sig)
ontofile.close()

print("\t".join(header))

for s in steps:
    print(s + "\t" + "\t".join(steps[s]))
