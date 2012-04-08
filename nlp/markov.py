#!/usr/bin/python

import sys, fileinput

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

bi = []
tri = []
def eat_next(word):
    if len(bi) = 2:


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
