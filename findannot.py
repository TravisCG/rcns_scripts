#!/usr/bin/python3

import sys
import gzip

def parse(csq):
    ret = dict()
    keys = {"cons":1, "gene":3, "clinsig": 62, "motif_name":66, "motif_score":69, "pheno":70, "gerp":71, "gerprs":72, "provean":73, "clinvar":75, "clinvarrs":77}
    for k in keys:
        ret[k] = set()
    fields = csq.split(",")
    for i in fields:
        annot = i.split("|")
        for k in keys:
            if annot[keys[k]] != "":
                ret[k].add(annot[keys[k]])
    return(ret)

def printres(gt, annot):
    print(gt, end = "\t")
    for i in ["cons", "gene", "clinsig", "motif_name", "motif_score", "pheno", "gerp", "gerprs", "provean", "clinvar", "clinvarrs"]:
        print(",".join(list(annot[i])), end = "\t")
    print()

gt = dict()

for i in open(sys.argv[1]):
    fields = i.rstrip().split("\t")
    gt[fields[1]] = i.rstrip()

for i in gzip.open(sys.argv[2]):
    line = i.decode('utf-8').rstrip()
    if line.startswith("#"):
        continue
    fields = line.split("\t")
    if fields[2] in gt:
        # processing annotation
        info = fields[7]
        for j in info.split(";"):
            if j.startswith("CSQ"):
                important = parse(j)
                printres(gt[fields[2]], important)
                break
