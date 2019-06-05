#!/bin/bash

for i in G* S*
do
	cd $i
	for fasta in *_1.fq.gz
	do
		bwa mem /data/genomes/human/hg38 -t 6 $fasta ${fasta%_1.fq.gz}_2.fq.gz
		#rm $fasta ${fasta%_1.fq.gz}_2.fq.gz
	done | samtools view -b -F 4 - >../${i}.bam
	cd ..
done
