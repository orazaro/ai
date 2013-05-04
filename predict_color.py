#!/usr/bin/env python
# emulate experiment with cards:
# from 52 cards you guess which will be red or can pass
# after your guess card is shown
#
# wining strategy: if so far reds was less than blacks guess red, else pass

import random
import numpy as np

random.seed()

n = 52
m = 1000
scores = []
for j in range(m):
    cards = range(n)
    random.shuffle(cards)
    reds = [(e%2*2)-1 for e in cards]
    score = 0
    sum = 0
    for i in range(n):
        if sum < 0:
            score += reds[i]
        sum += reds[i]
    print "%d" % score,
    scores.append(score)
print
scores = np.array(scores)
print "scores= %f +- %f" % (scores.mean(), scores.std())
