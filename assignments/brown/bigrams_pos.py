"""
Print bigrams where first word is adjective and second word is noun

typical usage:

% python3 bigrams_pos.py ../../data/brown_txt/*.txt > bigrams_pos_JN.tsv

each output line corresponds to a bigram:

word_A word_B frequency_of_bigram
"""


import sys
import re
from collections import defaultdict


def tokenize(line, l_n):
    '''Return a list of tokens and POS values extracted from line'''
    tokens = []
    poses = []
    for j, word in enumerate(line.rstrip().split()):
        fields = word.split('/')
        if len(fields) != 2:
            print(
                f'Bad input: word "{word}", which is the {j + 1}-th word in line {l_n + 1}')
            sys.exit(1)
        token, pos = word.split('/')
        tokens.append(token)
        poses.append(pos)
    return tokens, poses


def dofile(fname, bigramfreq, regex1, regex2):
    '''Read a corpus and update bigram frequencies if the tokens that comprise the
    bigram have the appropriate POS tags.'''
    for i, line in enumerate(open(fname, encoding='utf-8', errors='surrogateescape')):
        sentence, pos = tokenize(line, i)
        for j in range(len(sentence) - 1):
            if re.match(regex1, pos[j]) and re.match(regex2, pos[j+1]):
                bigram = f"{sentence[j]}\t{sentence[j+1]}"
                bigramfreq[bigram] += 1


def bigrams_pos():
    """Main function that prints bigrams where first word is adjective and second word is noun"""
    # first word is adjective
    regex_pos1 = "JJ.*"
    # second word is noun
    regex_pos2 = "N.*"

    # bigram frequencies { bigram_form : freq }
    bigramfreq = defaultdict(int)
    for fname in sys.argv[1:]:
        print(fname, file=sys.stderr)
        # update bigram freqs and word freqs
        dofile(fname, bigramfreq, regex_pos1, regex_pos2)

        sorted_bigramfreq = dict(sorted(bigramfreq.items(), key=lambda item: item[1], reverse=True))

    for bigram, fbigram in sorted_bigramfreq.items():
        print(f"{bigram}\t{fbigram}")


if __name__ == "__main__":
    bigrams_pos()
