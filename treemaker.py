#!/usr/bin/python3

import glob
import sys
import re
import os

def getseq(filename, idx, sample):
    fasta = open(filename)
    readseq = False
    seq = ">" + sample + "\n"
    for i in fasta:
        if readseq and i.startswith('>'):
            break
        if idx in i:
            readseq = True
            continue
        if readseq:
            seq = seq + i
    fasta.close()
    return seq

gene = sys.argv[1]
idre = re.compile("ID=([^;]+);")

files = glob.glob('*.gff', recursive = True)
out = open(gene + ".fasta", "w")
for i in files:
    gff = open(i)
    sample = i.split("/")[0]
    for line in gff:
        if "Name=" + gene + ";" in line:
            match = idre.search(line)
            if match:
                idx = match.group(1)
                seq = getseq(i.replace("gff","faa"), idx, sample)
                out.write(seq)
    gff.close()
out.close()

os.system("mafft --localpair --maxiterate 3000 --thread 10 --clustalout --treeout --reorder "+gene+".fasta >" + gene + ".mafft")
