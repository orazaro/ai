#!/bin/sh
zcat ../data/dreiser.txt.gz |tr -cs 'a-zA-Z0-9' '\n'|tr 'A-Z' 'a-z'|sort|uniq -c|sort -nr|wc -l
