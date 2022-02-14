#!/usr/bin/env python3

# Given a list of files create a document frequency file.
#
# typical usage:
#
# % python3 df.py gutenberg/*.txt > word.df
#
# output has the following format:
#
# - first line is the total number of documents
# - then, for each word
#
#   word TAB number_of_documents_where_the_word_appears
#
# for example:
#
# 18
# length	14
# excusable	3
# leave-taking	2
# sleek	5
# absented	1
# visited	11
# parley	6
# Otways	1
# discharged	7

import sys
from collections import defaultdict

def tokenize(line):
    '''Return a list with tokens in line'''
    return line.rstrip().split()

def do_file(fname, word_docfreq):
    '''Read file and update word_docfreq dictionary.'''
    document_words = set() # a set with the words in the document
    for line in open(fname, encoding='utf-8', errors='surrogate'):
        sentence = tokenize(line)
        # TODO
        # insert each sentence word in 'document_words' set
        #
        # - use the 'add' method to insert new elements in a set. For
        #   example, the following line:
        #
        #   document_words.add('hello')
        #
        #   adds the word 'hello' to the 'document_words' set.
        pass # REMOVE THIS LINE
        # ENDTODO
    # TODO: Once we've recorded all the words in the document, update
    #       'word_docfreq' with the words in 'document_words'
    pass # REMOVE THIS LINE
    # ENDTODO

word_docfreq = defaultdict(int) # (word -> number_of_documents_where_the_word_appears)
number_documents = 0
for fname in sys.argv[1:]:
    number_documents += 1
    do_file(fname, word_docfreq)

print(number_documents) # first line is the number of documents
for word, freq in word_docfreq.items():
    print("{}\t{}".format(word, freq))
