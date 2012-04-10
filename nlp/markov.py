#!/usr/bin/python

import sys, random

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def eat_next(lm, word, phrase):
    key = '_'.join(phrase)
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
    phrase.pop(0)
    phrase.append(word)

def read(lm, ngrams):
    phrase = ['<UNK>'] * (ngrams - 1)
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
            eat_next(lm, word.lower(), phrase)

def select(wdic):
    n = 0
    sel = []
    for k in wdic:
        for i in range(wdic[k]):
            sel.append(k)
    n = random.randint(0,len(sel)-1)
    return sel[n]

def generate(lm, keys, phrase):
    if not phrase:
        n = random.randint(0,len(keys)-1)
        key = keys[n]
        words = key.split('_')
        for w in words:
            phrase.append(w)
    else:
        key = '_'.join(phrase)
    if key not in lm:
        return '<END>'
    #print key, lm[key]
    p = lm[key]
    word = select(p)
    phrase.pop(0)
    phrase.append(word)
    if len(p) > 1:
        return '*'+word
    return word


ngrams = 4
if len(sys.argv) > 1:
    ngrams = int(sys.argv[1])

language_model = {}
read(language_model, ngrams)

keys = language_model.keys()
phrase = []
word = '<START>'
try:
    while word != '<END>':
        word = generate(language_model, keys, phrase)
        print word,
except:
    print ' <ABORTED>'

