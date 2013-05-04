#!/usr/bin/env python
# emulate experiment with cards:
# from 52 cards you guess which will be red or can pass
# after your guess card is shown
#
# wining strategy: if so far reds was less than blacks guess red, else pass
# it works if summarize winning reds, but if you win/lose after first selection
# and finally must select last card if do not selected before: 
# no winning strategy

import random
import numpy as np

random.seed()

n = 52
m = 100000
scores = []
for j in range(m):
    cards = range(n)
    random.shuffle(cards)
    reds = [(e%2*2)-1 for e in cards]
    score = 0
    sum = 0
    for i in range(n):
        if sum < 0 or i == n-1:
            score += reds[i]
            break
        sum += reds[i]
    #print "%d" % score,
    scores.append(score)
print
scores = np.array(scores)
print "scores= %f +- %f" % (scores.mean(), scores.std())
