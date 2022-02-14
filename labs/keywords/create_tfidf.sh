#!/bin/bash

# Usage: ./create_tfidf.sh

inDir=../../data/gutenberg
outDir=out
dfFile=word.df

if [ ! -d ${inDir} ] ; then
	echo "Input directory ${inDir} does not exist!"
	exit 1
fi

if [ ! -e ${dfFile} ] ; then
	echo "${dfFile} does not exist!"
	exit 1
fi

if [ ! -d ${outDir} ] ; then
    mkdir ${outDir}
fi

for infile in ${inDir}/*.txt; do
	bname=$(basename ${infile} .txt)
	outfile=${outDir}/${bname}.tfidf
	echo "${infile} -> ${outfile}"
	python3 tfidf.py ${dfFile} ${infile} > ${outfile}
done

# Create similarity matrix

python3 docSimilarityMatrix.py out/* > docsim.csv
