#!/usr/bin/python3

import sys

out = open(sys.argv[2], "w")
f = open(sys.argv[1])
out.write(f.readline())
for i in f:
    fields = i.rstrip().split("\t")
    if "intron_variant" in fields[12] or fields[12] == "upstream_gene_variant" or fields[12] == "downstream_gene_variant" or fields[12] == "synonymous_variant" or "UTR" in fields[12]:
        continue
    gt = [int(j) for j in fields[5:12]]
    if sum(gt) == 0:
        continue
    out.write("\t".join(fields) + "\n")
out.close()
