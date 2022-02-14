#!/usr/bin/env python3

# create a vector of words with tdidf for a document. Needs two files: df list and a document
#
# typical usage:
#
# % python3 tfidf.py word.df gutenberg/austen-emma.txt
#
# output has the following format:
#
# word TAB tfidf
#
# for example:
#
# Emma	14.861774159366927
# Jane	10.23171168171714
# Austen	1.2419530243370103
# 1816	2.003453034755819
# VOLUME	4.006906069511638
# CHAPTER	4.422300833652587
# Woodhouse	16.617883111515514
# handsome	1.7914256461824325
# clever	1.9586253758076808
# rich	0.15478785409395548

import sys
from collections import defaultdict
from math import log

def tokenize(line):
    '''Return a list with tokens in line'''
    return line.rstrip().split()

def tf(fname):
    '''Read corpus and compute word frequencies.'''
    wordfreq = defaultdict(float)
    for line in open(fname, encoding='utf-8', errors='surrogateescape'):
        for word in tokenize(line):
            wordfreq[word] += 1.0
    return wordfreq

def idf(df_fname):
    '''Read document and return a dictionary with (word -> idf) associations'''
    idf = {} # the dictionary
    fh = open(df_fname, encoding='utf-8', errors='surrogateescape')
    doc_n = float(fh.readline().rstrip()) # read first the number of documents
    for line in fh.readlines():
        fields = line.rstrip('\n').rstrip().split(sep="\t")
        if len(fields) < 2:
            continue # discard malformed lines
        word = fields[0]      # the word
        df = float(fields[1]) # the document frequency of the word
        # TODO calculate idf value and store in 'idf'
        #
        # Remember: idf = log(N/df), where N is the total number of
        #           documents (doc_freq), and df is the document frequency
        #           of the word
        #
        idf[word] = log(doc_n/df)
    return idf # return dictionary

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " word.df document.txt")
    exit(1)

df_fname = sys.argv[1]
doc_fname = sys.argv[2]

word_tf = tf(doc_fname)   # { word =>  tf}
word_idf = idf(df_fname)  # { word => idf }
tfidf = 0
for word in word_tf:
    if word not in word_idf:
        continue
    if word_idf[word] == 0:
        continue
    # TODO calculate tfifd value and store it in the tfidf variable
    tfidf = log(word_tf[word] + 1) * word_idf[word]
    print("{}\t{}".format(word, tfidf))
