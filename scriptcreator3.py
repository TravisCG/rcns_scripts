#!/usr/bin/python3

import sys

table = open(sys.argv[1])
table.readline()
exphash = dict()
for i in table:
	cols = i.rstrip().split("\t")
	if cols[0] not in exphash:
		exphash[cols[0]] = list()
	exphash[cols[0]].append(cols[1])

print("library(ggplot2)")
for i in exphash:
	print('subset <- read.table("%s.tsv", colClasses = c("factor","factor","double","factor","double"))' % i)
	print('colnames(subset) <- c("expid", "peak", "peakscore", "contains_target_motif", "height")')
	print('pdf("%s.pdf")' % i)
	print('ggplot(subset) + geom_violin(aes(x=contains_target_motif, y = height)) + scale_x_discrete(labels = c("other", "%s")) + ggtitle("Comparing peak height in four experiments") + ylab("Peak height") + xlab("Target motif")' % "+".join(exphash[i]))
	print('dev.off()')
