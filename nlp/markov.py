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
    for i in range(1,len(input)):
        input[i-1] = input[i]
    input[-1] = word

def generate(lm, keys, input = []):
    if not input:
        n = random.randint(0,len(keys)-1)
        key = keys[n]
        input = key.split('_')
    else:
        key = '_'.join(input)
    p = lm[key]
    n = 0
    sel = []
    for k in p:
        for i in range(p[k]):
            sel.append(k)
    n = random.randint(0,len(sel)-1)
    word = sel[n]
    for i in range(1,len(input)):
        input[i-1] = input[i]
    input[-1] = word
    return word


def read(lm, ngrams):
    input = ['none'] * (ngrams - 1)
    for line in fileinput.input():
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

ngrams = 4
language_model = {}
read(language_model, ngrams)
keys = []
for key in language_model:
    keys.append(key)
    print key, language_model[key]
input = []
while True:
    word = generate(language_model, keys, input)
    print word,

