#!/usr/bin/python3

import sys

"""
   Replace ids in one column based on another file
   Usage: colreplace.py -id idfile -input input.txt -colnum 8 -del "\t" >newfile.txt
   -id: id replace file. Tab delimited file with two columns. First is the old ID, second the new id.
   -input: input file
   -colnum: the number of column you want to change. Zero based
   -del: input and output file delimiter default: tab
"""

colnum = 7
delim = "\t"

for i in range(len(sys.argv)):
	if sys.argv[i] == "-id":
		idfile = sys.argv[i+1]
	if sys.argv[i] == "-input":
		inputfile = sys.argv[i+1]
	if sys.argv[i] == "-colnum":
		colnum = int(sys.argv[i+1])
	if sys.argv[i] == "-del":
		delim = sys.argv[i+1]

ids = dict()
idf = open(idfile)
if not idf:
	print("No id file!", file=sys.stderr)
	exit(1)
for i in idf:
	columns = i.rstrip().split("\t")
	if columns[0] in ids:
		print("Duplicated identifier!:", columns[0], file=sys.stderr)
	ids[columns[0]] = columns[1]

inp = open(inputfile)
if not inp:
	print("No input file", file = sys.stderr)
	exit(1)
for i in inp:
	columns = i.rstrip().split(delim)
	oldid = columns[colnum]
	if oldid not in ids:
		print("Woudn't replace:", oldid, file = sys.stderr)
		continue
	columns[colnum] = ids[oldid]
	print(delim.join(columns))
