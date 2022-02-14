#!/usr/bin/python3

import sys
from math import sqrt
import os.path

def vmod(v):
    '''return module of dictionary v'''
    mod = 0
    for c in v.values():
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

DocsTfIdf = {} # [ doc => tf_idf_vector ]
for fname in sys.argv[1:]:
    (bname, ext) = os.path.splitext(os.path.basename(fname))
    DocsTfIdf[bname] = readV(fname)

docs = DocsTfIdf.keys()
print("\"\",{}".format(",".join(docs)))
for doc in docs:
    r = []
    v1 = DocsTfIdf[doc]
    for doc2 in docs:
        v2 = DocsTfIdf[doc2]
        r.append(mycos(v1, v2))
    print("\"{}\"".format(doc), end=',')
    print(",".join("{:.2f}".format(x) for x in r))
