#!/usr/bin/python3

import sys

seq1 = sys.argv[1]
seq2 = sys.argv[2]

first = list()
second = list()

for i in open(sys.argv[3]):
	if i.startswith(seq1):
		first.append(i.rstrip().split()[1])
	if i.startswith(seq2):
		second.append(i.rstrip().split()[1])

if len(first) != len(second):
	print("Something wrong with the alignment")
else:
	mismatch = 0
	for i in range(len(first)):
		for j in range(len(first[i])):
			if first[i][j] != second[i][j]:
				mismatch += 1
				print(first[i][j], second[i][j])
	print(mismatch)
