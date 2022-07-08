import sys

def findN(header, seq):
	if seq[0] == 'N':
		start = 0
	for i in range(1,len(seq)):
		if seq[i] == 'N' and seq[i-1] != 'N':
			start = i
		if seq[i] != 'N' and seq[i-1] == 'N':
			print(header, start, i, sep = "\t")

header = ""
for i in open(sys.argv[1]):
	if i.startswith(">"):
		if header != "":
			findN(header, seq)
		header = i.rstrip()[1:]
		seq = ""
	else:
		seq = seq + i.rstrip()
