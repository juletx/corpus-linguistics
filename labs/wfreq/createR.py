#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    fh = sys.stdin
else:
    fh = open(sys.argv[1])

F = []
for line in fh:
    l = line.rstrip('\n').rstrip()
    if len(l.split()) == 2:
        (freq, word) = l.split()
        F.append(int(freq))
F.sort(reverse=True)
print("wfreq <- c({})".format(",".join(str(x) for x in F)))
