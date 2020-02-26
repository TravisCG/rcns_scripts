#!/usr/bin/python

import sys

def kmerprune(seq, kmerlist, kmersize):
	seq = "".join(seq)
	for i in range(len(seq)-kmersize):
		kmer = seq[i:i+kmersize]
		if kmer in kmerlist:
			kmerlist.remove(kmer)

seq = list()
kmersize = 100

for i in open(sys.argv[1]):
	if i.startswith('>'):
		continue
	else:
		seq.append(i.rstrip())

seq = "".join(seq)
kmerlist = set()

for i in range(len(seq)-kmersize):
	kmer = seq[i:i+kmersize]
	if 'N' in kmer:
		continue
	kmerlist.add(kmer)

seq = list()
header = ""
skip = False
for i in open(sys.argv[2]):
	if i.startswith('>'):
		header = i.rstrip()[1:]
		if header == 'chrY':
			skip = True
		else:
			skip = False
		if len(seq) > 0:
			kmerprune(seq, kmerlist, kmersize)
			seq = list()
	else:
		if not skip:
			seq.append(i.rstrip())
kmerprune(seq, kmerlist, kmersize)
for i in kmerlist:
	print(i)
