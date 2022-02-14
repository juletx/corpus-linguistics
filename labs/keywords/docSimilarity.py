#!/usr/bin/python3

import sys
from math import sqrt
import os.path

def vmod(v):
    '''return module of dictionary v'''
    mod = 0
    for w,c in v.items():
        mod += c * c
    return sqrt(mod)

def mycos(dd1, dd2):
    '''apply cosine similarity to two dictionaries'''
    d1 = dd1
    d2 = dd2
    if len(dd1) > len(dd2):
        d2 = dd1
        d1 = dd2
    # d1 contains the smallest dictionary
    mod1 = vmod(d1)
    mod2 = vmod(d2)
    if (mod1 * mod2) == 0:
        return 0
    result = 0
    for w, c1 in d1.items():
        if w not in d2:
            continue
        c2 = d2[w]
        result += c1 * c2
    return result / (mod1 * mod2)

def readV(fname):
    '''read tfifd file and return as a dictionary'''
    h = {}
    for line in open(fname, encoding='utf-8'):
        fields = line.rstrip('\n').rstrip().split(sep="\t")
        if len(fields) != 2:
            continue
        if fields[0] in h:
            continue
        h[fields[0]] = float(fields[1])
    return h

if len(sys.argv) != 3:
    print("Usage: pyhton3 docSimilarity.py file1.tfidf file2.tfidf")
    exit

v1 = readV(sys.argv[1])
v2 = readV(sys.argv[2])
sim = mycos(v1, v2)
print("Similarity: ", sim)
