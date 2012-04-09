#!/usr/bin/python

import sys, fileinput, random

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def eat_next(lm, word, input):
    key = '_'.join(input)
    #print key
    if key in lm:
        p = lm[key]
        if word in p:
            p[word] += 1
        else:
            p[word] = 1
    else:
        lm[key] = {}
        lm[key][word] = 1
    input.pop(0)
    input.append(word)

def read(lm, ngrams):
    input = ['none'] * (ngrams - 1)
    #for line in fileinput.input():
    for line in sys.stdin:
        words = []
        word = ''
        for c in line:
            if c in alpha:
                word += c
            else:
                if word:
                    words.append(word)
                    word = ''
        for word in words:
            eat_next(lm, word.lower(), input)

def generate(lm, keys, input = []):
    if not input:
        n = random.randint(0,len(keys)-1)
        key = keys[n]
        words = key.split('_')
        for w in words:
            input.append(w)
    else:
        key = '_'.join(input)
    #print key, lm[key]
    p = lm[key]
    n = 0
    sel = []
    for k in p:
        for i in range(p[k]):
            sel.append(k)
    n = random.randint(0,len(sel)-1)
    word = sel[n]
    input.pop(0)
    input.append(word)
    return word


ngrams = 4
if len(sys.argv) > 1:
    ngrams = int(sys.argv[1])
language_model = {}
read(language_model, ngrams)
keys = []
for key in language_model:
    keys.append(key)
    #print key, language_model[key]
input = []
while True:
    word = generate(language_model, keys, input)
    print word,

