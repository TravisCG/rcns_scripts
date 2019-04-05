#!/bin/bash

export LD_LIBRARY_PATH=/home/nagy.tibor/root-6.16.00/mybuild/lib

CNVNATOR=/home/nagy.tibor/CNVnator/cnvnator

SAMPLE=$1

cd /molbio/projects/rare_diseases/$SAMPLE

mkdir CNV

cd CNV

$CNVNATOR -root ${SAMPLE}.root -tree ../bam/${SAMPLE}_hg38.bq.bam
$CNVNATOR -root ${SAMPLE}.root -his 1000 -d /molbio/projects/rare_diseases/chrs
$CNVNATOR -root ${SAMPLE}.root -stat 1000
$CNVNATOR -root ${SAMPLE}.root -partition 1000
$CNVNATOR -root ${SAMPLE}.root -call 1000 >${SAMPLE}.out
