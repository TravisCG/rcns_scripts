#!/usr/bin/python3

"""
   Create a similarity matrix from Mauve alignment file
"""

import sys

def process_blocks(h, s, m):
    # Concatenate sequences
    for i in range(len(s)):
        s[i] = "".join(s[i])

    for a in range(len(s)-1):
        for b in range(a+1, len(s)):
            found = 0.0
            for pos in range(len(s[a])):
                if s[a][pos] == s[b][pos]:
                    found += 1.0
            found = found / float(len(s[a])) # similarity percentage
            if h[a] not in m:
                m[h[a]] = dict()
            if h[b] not in m[h[a]]:
                m[h[a]][h[b]] = list()
            m[h[a]][h[b]].append(found)

headers = list()
seqs    = list()
matrix  = dict()
allseq  = set()

for i in open(sys.argv[1]):
    if i.startswith("#"):
        continue
    if i.startswith(">"):
        # header
        idx = i.rstrip().split()[3].split("/")[-1]
        a   = list()
        headers.append(idx)
        seqs.append(a)
        allseq.add(idx)
        continue
    if i.startswith("="):
        # end of the alignment block
        process_blocks(headers, seqs, matrix)
        headers = list()
        seqs    = list()
        continue
    seqs[-1].append(i.rstrip())

allseq = list(allseq)

print("\t".join(allseq))
for a in allseq:
    out = list()
    out.append(a)
    for b in allseq:
        if a in matrix and b in matrix[a]:
            avg = sum(matrix[a][b]) / float(len(matrix[a][b]))
            out.append(str(avg))
        elif a == b:
            out.append("1")
        elif b in matrix and a in matrix[b]:
            avg = sum(matrix[b][a]) / float(len(matrix[b][a]))
            out.append(str(avg))
        else:
            out.append("0")
    print("\t".join(out))
