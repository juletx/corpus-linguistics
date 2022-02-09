#!/usr/bin/env python3

# count words by using spacy tokenizer
#
# NOTE: you need to download the English model first. Just run the following
# command:
#
# python3 -m spacy download en
#

import sys
import spacy
from collections import defaultdict


def tokenize(line):
    '''Return a list with tokens in line'''
    # TODO tokenize using spacy
    doc = nlp(line)
    return doc


def do_file(filename, wordfreq):
    for line in open(filename, encoding='utf-8', errors='surrogate'):
        for token in tokenize(line):
            # TODO: increment the frequency of token
            wordfreq[token.text] += 1


# TODO initialize spacy with 'en' model
nlp = spacy.load("en_core_web_sm")

wordfreq = defaultdict(int)
for fname in sys.argv[1:]:
    do_file(fname, wordfreq)

for word, freq in wordfreq.items():
    print("{}\t{}".format(freq, word))
