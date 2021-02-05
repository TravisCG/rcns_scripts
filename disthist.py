#!/usr/bin/python3

"""
   Very simple split-read analyser
   Only use reads which has the same
   orientation as the reference
   The reference should be a single fasta file
   Right now it is working only if the read length is 150 bp

   Usage: disthist.py reference.fasta fastq1.gz fastq2.gz
"""

import sys
import gzip

def decision(left, right, hashlist):
	if left in hashlist and right not in hashlist:
		print(hashlist[left], "onlyleft")
	if left not in hashlist and right in hashlist:
		print(hashlist[right], "onlyright")
	if left in hashlist and right in hashlist:
		all_lpos = hashlist[left]
		all_rpos = hashlist[right]
		for lpos in all_lpos:
			for rpos in all_rpos:
				if rpos - lpos == 100:
					return
		if len(hashlist[left]) == 1 and len(hashlist[right]) == 1:
			print(hashlist[left][0], hashlist[right][0], "distanceanomaly")

hashlist = dict()
hashlen  = 50

fastafile = open(sys.argv[1])
fastafile.readline()

fasta = list()
for i in fastafile:
	fasta.append(i.rstrip())

fasta = "".join(fasta)
for i in range(len(fasta) - hashlen):
	subseq = fasta[i:i+hashlen]
	if 'N' in subseq:
		continue
	if subseq not in hashlist:
		hashlist[subseq] = list()
	hashlist[subseq].append(i)

for filename in sys.argv[2:]:
	fastqfile = gzip.open(filename)
	count = 0
	for i in fastqfile:
		if count % 4 == 1:
			seq = i.decode('utf-8').rstrip()
			left = seq[:hashlen]
			right = seq[-hashlen:]
			decision(left, right, hashlist)
		count += 1
	fastqfile.close()
