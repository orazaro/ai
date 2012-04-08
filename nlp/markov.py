#!/usr/bin/python

import sys, fileinput, random

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

bi_list = ['none']
bi = {}
bis = []

def eat_next(word):
    global bi_list
    global bi
    bip = bi_list[0]
    bi_list = [word]
    if bip in bi:
        p = bi[bip]
        if word in p:
            p[word] += 1
        else:
            p[word] = 1
    else:
        bi[bip] = {}
        bi[bip][word]=1
        bis.append(bip)

def gen_bi(word = ''):
    if word == '':
        n = random.randint(0,len(bis))
        word = bis[n]
    p = bi[word]
    n = 0
    sel = []
    for k in p:
        for i in range(p[k]):
            sel.append(k)
    n = random.randint(0,len(sel)-1)
    return sel[n]



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
        eat_next(word.lower())

word = ''
while True:
    word = gen_bi(word)
    print word,

