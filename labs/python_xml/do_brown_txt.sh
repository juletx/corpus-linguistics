#!/bin/bash

inDir=brown_tei
outDir=brown_txt

if [ ! -d ${outDir} ] ; then
    mkdir ${outDir}
fi

if [ ! -d ${inDir} ] ; then
	echo "Input directory ${inDir} does not exist!"
	exit 1
fi

cmd="python3 brown2txt.py"

for fname in ${inDir}/*.xml; do
	bname=`basename ${fname} .xml`
	echo "${cmd} ${fname} > ${outDir}/${bname}.txt"
	${cmd} ${fname} > ${outDir}/${bname}.txt
done
