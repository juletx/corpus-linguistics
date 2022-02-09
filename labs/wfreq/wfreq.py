#!/usr/bin/env python3

# Usage:
#
# python3 wfreq.py gutenberg/* > wfreq.list

import sys
from collections import defaultdict


def tokenize(line):
    '''Return a list with tokens in line'''
    return line.rstrip().split()


def do_file(filename, wordfreq):
    for line in open(filename, encoding='utf-8', errors='surrogate'):
        for token in tokenize(line):
            # TODO: increment the frequency of token
            wordfreq[token] += 1


wordfreq = defaultdict(int)
for fname in sys.argv[1:]:
    do_file(fname, wordfreq)

for word, freq in wordfreq.items():
    print("{}\t{}".format(freq, word))
