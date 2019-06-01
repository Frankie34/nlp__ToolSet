#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:45:26 2019

@author: junchengzhu
"""

import nltk
from nltk.corpus import brown



#'''

#  Incrementally Updating a Dictionary  #

from collections import defaultdict
counts = defaultdict(int)
for (word, tag) in brown.tagged_words(categories='news', tagset='universal'):
    counts[word] += 1
# print (counts)

from operator import itemgetter
sorted(counts.items(), key=itemgetter(1), reverse=False)
# print([t for t, c in sorted(counts.items(), key=itemgetter(1), reverse=False)])



#  we index words according to their last two letter  #
last_letters = defaultdict(list)
for (word, tag) in brown.tagged_words(categories='news', tagset='universal'):
     key = word[0:2]
     last_letters[key].append(word)

# print(last_letters['ly'])
     
     
#  Tagging  #
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

size = int(len(brown_tagged_sents) * 0.9)

train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)


from pickle import dump
output = open('t2.pkl', 'wb')
dump(t2, output, -1)
output.close()


 	
from pickle import load
input = open('t2.pkl', 'rb')
tagger = load(input)
input.close()


#  Noun Phrase Chunking  #

text = """The board's action shows what free enterprise
     is up against in our complex maze of regulatory laws ."""
     

tokens = text.split()
sentence = tagger.tag(tokens)

grammar = "NP: {<DT>?<JJ>*<NN>}"

cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence) 
print(result) 

result.draw()





