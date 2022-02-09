#!/usr/bin/env python3

# print bigrams where first word is adjective and second word is noun
#
# typical usage:
#
# % python3 bigrams_pos.py gutenberg_pos/*.txt > bigrams_pos.txt
#
# each output line corresponds to a bigram:
#
# word_A word_B frequency_of_bigram
#
# for example, for the noun-noun case:
#
# [	Emma	1
# Jane	Austen	3
# Emma	Woodhouse	4
# Miss	Taylor	48
# Mr.	Woodhouse	135
# means	rank	1
# Mr.	Weston	167
# tenderer	recollection	1
# Mrs.	Weston	256
# November	evening	1

import sys
import re
from collections import defaultdict


def get_bigram(wA, wB):
    '''Create a string with the bigram formed by two tokens'''
    return "{}\t{}".format(wA, wB)


def tokenize(line, l_n):
    '''Return a list of tokens and POS values extracted from line'''
    tokens = []
    poses = []
    for j, w in enumerate(line.rstrip().split()):
        fields = w.split('/')
        if len(fields) != 2:
            print(
                f'Bad input: word "{w}", which is the {j + 1}-th word in line {l_n + 1}')
            exit(1)
        t, p = w.split('/')
        tokens.append(t)
        poses.append(p)
    return tokens, poses


def dofile(fname, bigramfreq, regex1, regex2):
    '''Read a corpus and update bigram frequencies if the tokens that comprise the
    bigram have the appropriate POS tags. '''
    for i, line in enumerate(open(fname, encoding='utf-8', errors='surrogateescape')):
        sentence, pos = tokenize(line, i)
        # TODO:
        # - iterate sentence and for each bigram:
        #   - get pair of words to create the bigram
        #   - increment in one the frequency of the bigram (in bigramfreq)
        #     if the words that compose the bigram have the appropriate POS
        #     tags
        #
        # Hints:
        #
        #  - use a for loop to iterate over indices of sentence.
        #
        #  - given index i:
        #     sentence[i]: ith token of the sentence
        #
        #  - Given tokens t1 and t2, use get_bigram(t1, t2) to obtain the bigram string
        #
        #  - re.search(regex, pos): returns True if string 'pos' matches the
        #    regular expression in 'regex'
        for i in range(len(sentence) - 1):
            if re.match(regex1, pos[i]) and re.match(regex2, pos[i+1]):
                bigram = get_bigram(sentence[i], sentence[i+1])
                bigramfreq[bigram] += 1


# TODO: first word is adjective
regex_pos1 = "G"
# TODO: second word is noun
regex_pos2 = "N|R"

bigramfreq = defaultdict(int)  # bigram frequencies { bigram_form : freq }
for fname in sys.argv[1:]:
    print(fname, file=sys.stderr)
    # update bigram freqs and word freqs
    dofile(fname, bigramfreq, regex_pos1, regex_pos2)

for bigram, fbigram in bigramfreq.items():
    print("{}\t{}".format(bigram, fbigram))
