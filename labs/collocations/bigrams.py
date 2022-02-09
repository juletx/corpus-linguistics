#!/usr/bin/env python3

# create a file with bigram counts. Needs a list of files with a tabulated input of corpus
#
# typical usage:
#
# % python3 bigrams.py gutenberg/* > bigrams.txt
#
# output has the following format:
#
# - first line is number of bigrams and number of tokens
# - then, one line per bigram with the following format:
#
#   word1 word2 bigram_frequency word1_frequency word2_frequency
#
# for example
#
# 2447528	2543758
# [	Emma	1	131	866
# Emma	by	1	866	7981
# by	Jane	4	7981	303
# Jane	Austen	3	303	3
# Austen	1816	1	3	1
# 1816	]	1	1	131
# VOLUME	I	1	3	29222
# CHAPTER	I	4	291	29222
# Emma	Woodhouse	4	866	313

import sys
from collections import defaultdict


def get_bigram(wA, wB):
    '''Create a string with the bigram formed by two tokens'''
    return "{}\t{}".format(wA, wB)


def tokenize(line):
    '''Return a list with tokens in line'''
    return line.rstrip().split()


def dofile(fname, bigramfreq, wordfreq):
    '''Read a corpus and update bigram and word frequencies.'''
    for line in open(fname, encoding='utf-8', errors='surrogateescape'):
        sentence = tokenize(line)
        # TODO:
        # - iterate sentence and for each bigram:
        #   - get pair of words to create the bigram
        #   - increment in one the frequency of the bigram (in bigramfreq)
        #   - increment in one the frequency of the first word (in wordfreq)
        #
        # Hints:
        #  - use a for loop to iterate over indices of sentence
        #  - given index i:
        #     sentence[i]: ith token of the sentence
        #  - Given tokens t1 and t2, use get_bigram(t1, t2) to obtain the bigram string
        for i in range(len(sentence) - 1):
            bigram = get_bigram(sentence[i], sentence[i+1])
            bigramfreq[bigram] += 1
            wordfreq[sentence[i]] += 1
        wordfreq[sentence[len(sentence) - 1]] += 1


wordfreq = defaultdict(int)    # word frequencies { word_form : freq }
bigramfreq = defaultdict(int)  # bigram frequencies { bigram_form : freq }
for fname in sys.argv[1:]:
    print(fname, file=sys.stderr)
    dofile(fname, bigramfreq, wordfreq)  # update bigram freqs and word freqs

# count total words
word_total = 0
for w, c in wordfreq.items():
    word_total += c
# count total bigrams
big_total = 0
for b, c in bigramfreq.items():
    big_total += c

# print output
# first line is number of bigrams and number of words
print("{}\t{}".format(big_total, word_total))
# for each bigram
#     word1 word2 count_big count_A count_B
for bigram, fbigram in bigramfreq.items():
    word1, word2 = bigram.split('\t')
    fword1 = wordfreq[word1]
    fword2 = wordfreq[word2]
    print("{}\t{}\t{}\t{}".format(bigram, fbigram, fword1, fword2))
