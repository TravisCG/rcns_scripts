#!/usr/bin/python3

"""
   Usage: vcffiltbygene.py genelist.txt input.vcf output.tsv
   There is a drawback: the script not try to determine the
   number of samples!
"""

import gzip
import sys

def getannot(raw, symbols):
    chunks = raw.split(";")
    for c in chunks:
        if "=" not in c:
            continue
        key, value = c.split("=")
        if key == "CSQ":
            for v in value.split(","):
                annots = v.split("|")
                if annots[3] in symbols:
                    if annots[43] == "":
                        annots[43] = "0.0"
                    return([annots[1], annots[2], annots[3], annots[43]])
    return(["NA", "NA", "NA", "NA"])

genes = set()
for i in open(sys.argv[1]):
    genes.add(i.rstrip().split()[0])

out = open(sys.argv[3], "w")
for i in gzip.open(sys.argv[2]):
    line = i.decode("utf-8").rstrip()
    if line.startswith("##"):
        continue
    line = line.split("\t")
    if line[6] != "PASS":
        if line[0].startswith("#"):
            out.write("chr\tpos\tid\tref\talt\t" + "\t".join(line[9:16]) + "\teffect\timpact\tsymbol\t1000G_AF\n") # set the samples column range here!
        continue
    annotation = getannot(line[7], genes)
    samples = [j.split(":")[0] for j in line[9:16]] # set the samples column range here!
    for s in range(len(samples)):
        if samples[s][0] == "0" or samples[s][0] == ".":
            if samples[s][2] == "1":
                samples[s] = "1"
            else:
                samples[s] = "0"
        else:
            samples[s] = "2"
    if annotation[0] != "NA":
        output = line[0:5] + samples + annotation
        out.write("\t".join(output) + "\n")
out.close()
