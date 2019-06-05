#!/bin/bash

for D in *
do
	if [ -d $D ]
	then
		cd $D
		python3 /home/nagytibi/relaxaz/upload/M2a_WGS/gbk4submit.py *.gbk $D
		tbl2asn -p . -t /home/nagytibi/relaxaz/upload/M2a_WGS/template.sbt -M n -Z discrep
		cd ..
	fi
done
