#!/usr/bin/env python3
#
# Calculate PMI values of bigrams
#
# takes the output file of 'bigram.py' script as input.
# produces one line per bigram:
#
# word1 word2 pmi
#
# for example:
#
# $ python3 pmi.py bigrams.txt
#
# Woodhouse	,	1.5681011844369697
# handsome	,	1.077318637449991
# ,	and	1.8817064464899467
# rich	,	0.6565840143063624
# ,	with	0.4618216223142664
# with	a	2.03849919937966
# home	and	0.012635069922425135
# and	happy	0.5589779962941499
# disposition	,	1.2489326244458483
# ,	seemed	0.05595061444113458

import sys
from math import log


def parse_line(line):
    ''' Parse a line and extract fields.'''
    fields = line.rstrip().split()
    word1, word2 = fields[0:2]
    bigram_freq, word1_freq, word2_freq = [float(x) for x in fields[2:]]
    return word1, word2, bigram_freq, word1_freq, word2_freq


def calc_pmi(bigram_freq, word1_freq, word2_freq, big_total, word_total):
    ''' Calculate the PMI value of a bigram.'''
    # TODO: calculate PMI
    return log(big_total) + log(bigram_freq) - log(word1_freq) - log(word2_freq)


if len(sys.argv) > 1:
    fh = open(sys.argv[1], encoding='utf-8')
else:
    fh = sys.stdin

cut_N = 3
# read total bigrams, words
big_total, word_total = [float(x) for x in fh.readline().rstrip().split()]
for line in fh.readlines():
    word1, word2, bigram_freq, word1_freq, word2_freq = parse_line(line)
    # TODO: discard bigram if frequency is small
    if bigram_freq >= cut_N:
        pmi = calc_pmi(bigram_freq, word1_freq,
                       word2_freq, big_total, word_total)
        print("{}\t{}\t{}".format(word1, word2, pmi))
