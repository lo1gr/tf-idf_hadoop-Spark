#!/usr/bin/env python

from operator import itemgetter
import sys
from math import log10, sqrt

prev_word = None
count = 1
word = None
df = {}
l1 = []
D = 10.0
tfidf=0

# input: <word, <documentNamed#n#N#1>>
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    w, z = line.split('\t', 1)
    f, nNc = z.split(' ', 1)
    n, Nc = nNc.split(' ', 1)
    N, c = Nc.split(' ', 1)
    if prev_word == w:
        count = count + int(c)  # count occurences of word in all the docs
    else:
        if prev_word != None:
            q = n + ' ' + N + ' ' + str(count)
            df[prev_word] = q
            j = prev_word + ' ' + f
            l1.append(j)
        count = 1
        prev_word = w

q = n + ' ' + N + ' ' + str(count)
df[prev_word] = q
j = prev_word + ' ' + f
l1.append(j)

# l1: word#f
# df: {word: n#N#count}

for h in l1:
    w, f = h.split(' ', 1)
    for d in df:
        if w == d:
            n, N, m = df[d].split(' ', 2)
            n = float(n)
            N = float(N)
            m = float(m)
            tfidf = (n / N) * log10(D / m)

            print '%s\t%s' % (h, tfidf)  # <<word#documentName>, <tfidf>>
