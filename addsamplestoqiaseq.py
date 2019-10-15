#!/usr/bin/python3

import glob
import re

patt = re.compile("_S[0-9]+_L00[0-9]_R1_001.fastq.gz")

files = glob.glob("*R1*.fastq.gz")
for f in files:
	base = re.sub(patt,"",f)
	print("[%s]" % (base))
	print("readFile1 = /srv/qgen/patients/%s" % (f))
	print("readFile2 = /srv/qgen/patients/%s" % (f.replace("_R1_", "_R2_")))
	print("intsrument = MiSeq")
	print("primerFile = /srv/qgen/patients/CDHS-18017Z-139.primers.txt")
	print("roiBedFile = /srv/qgen/patients/CDHS-18017Z-139.roi.bed")
	print("platform = Illumina\nrunCNV = False\nsampleType =  Single\nduplex = False\n")
