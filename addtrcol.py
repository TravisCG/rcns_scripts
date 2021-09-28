#!/usr/bin/python3

"""
   Add a new column based on a dictionary
"""

import sys

def printhelp():
	print("Usage:")
	print("python3 addtrcol.py -i input.tsv -t replace.tsv -o 2 -d \";\" -e NewColumn -c 1 -m None\t")
	print("!!All files should use the same delimiter character!!\n")
	print("-d: delimiter character. Default is TAB")
	print("-i: input file name, you will add new column to this file")
	print("-t: translate file name. The first column in this file is the key, the second one is the value")
	print("-o: Number of the new, inserted column. Zero based")
	print("-h: This help message")
	print("-e: If you use this argument, the program assume the input file has header. You can specify name of the new column")
	print("-c: Index of the column to use as a key (the values of this column can be found in the first column of the translate file)")
	print("-m: Missing value. If the key cannot be found in the translate file, the program use this value")
	sys.exit(0)

delim = "\t"
header = False
colname = "new_column"
mvalue = "MISSING"

for i in range(len(sys.argv)):
	if sys.argv[i] == "-t":
		trfilename = sys.argv[i+1]
	if sys.argv[i] == "-d":
		delim = sys.argv[i+1]
	if sys.argv[i] == "-o":
		outcolumn = int(sys.argv[i+1])
	if sys.argv[i] == "-h":
		printhelp()
	if sys.argv[i] == "-i":
		inputfilename = sys.argv[i+1]
	if sys.argv[i] == "-e":
		header = True
		colname = sys.argv[i+1]
	if sys.argv[i] == "-c":
		inputcolumn = int(sys.argv[i+1])
	if sys.argv[i] == "-m":
		mvalue = sys.argv[i+1]

tr = dict()
for i in open(trfilename):
	cols = i.rstrip().split(delim)
	tr[cols[0]] = cols[1]

inputfile = open(inputfilename)
if header:
	cols = inputfile.readline().rstrip().split(delim)
	cols.insert(outcolumn, colname)
	print(delim.join(cols))

for i in inputfile:
	cols = i.rstrip().split(delim)
	if cols[inputcolumn] in tr:
		cols.insert(outcolumn, tr[cols[inputcolumn]])
	else:
		cols.insert(outcolumn, mvalue)
		print("Missing value:", cols[inputcolumn], file=sys.stderr)
	print(delim.join(cols))
