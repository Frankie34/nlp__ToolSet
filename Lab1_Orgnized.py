#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 01:48:53 2019
cs224_NLP_2019_Lab_1
@author: junchengzhu
"""

# import my own corpus #
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/Users/junchengzhu/Lecture/nlp2019/Lab/Lab1/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
#print(wordlists.fileids())
#print(wordlists.words('TED.txt'))
'''
# get text length #

text = wordlists.words('TED.txt')
text2 = wordlists.words('PRINCE.txt')
text3 = wordlists.words('PRINCE2.txt')

# print(len(text))
# print(sorted(set(text)))
# print(len(set(text)))


# stopwords #

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

# print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))

from nltk.corpus import stopwords

stopwords.words('english')

def content_fraction(text):
     stopwords = nltk.corpus.stopwords.words('english')
     content = [w for w in text if w.lower() not in stopwords]
     return len(content) / len(text)


# print(content_fraction(wordlists.words('TED.txt')))


# Counting Words by Genre #

import nltk

from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist(
           (genre, word)
           for genre in brown.categories()
           for word in brown.words(categories=genre))

genre_word = [(genre, word) 
               for genre in ['speech']
               for word in text]
genre_word += [(genre, word) 
                   for genre in ['novel']
                   for word in text2]
genre_word += [(genre, word) 
                   for genre in ['fiction']
                   for word in text3]

# print(len(genre_word))

# print(genre_word[:4])

# print(genre_word[-4:])

from collections import defaultdict
counts = defaultdict(int)

for (genre, word) in genre_word:
    if((genre == 'speech')):
        counts[genre] += 1

for (genre, word) in genre_word:
    if((genre == 'novel')):
        counts[genre] += 1
        
for (genre, word) in genre_word:
    if((genre == 'fiction')):
        counts[genre] += 1
'''
'''
# the out put of the Counting Words
print("speech")
print(counts['speech'])

print("novel")
print(counts['novel'])

print("science fiction/ Love Story")
print(counts['fiction'])
'''

''' 
# the code below goes with the frequency of the word ever show up

cfd = nltk.ConditionalFreqDist(genre_word)


print(cfd.conditions())
print(cfd['romance'].most_common(20))

 	
print(cfd['news'])

print(cfd['romance'])

print(cfd['romance'].most_common(20))

cfd['romance']['could']
'''
'''
from nltk.corpus import inaugural
cfd = nltk.ConditionalFreqDist(
          (target, fileid[:4]) 
          for fileid in inaugural.fileids()
          for w in inaugural.words(fileid)
          for target in ['america', 'citizen'] 
          if w.lower().startswith(target))

'''
'''
from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch',
    'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
          (lang, len(word)) 
          for lang in languages
          for word in udhr.words(lang + '-Latin1'))


cfd.tabulate(conditions=['English', 'German_Deutsch'],
             samples=range(10), cumulative=True)

cfd.plot(conditions=['English', 'German_Deutsch'],
             samples=range(10), cumulative=True)
'''

# plot #
cfd = nltk.ConditionalFreqDist(
 (target, fileid)
 for fileid in wordlists.fileids()
 for w in wordlists.words(fileid)
 for target in ['can', 'could', 'may', 'might', 'must', 'will']
 if w.lower().startswith(target)) 



cfd.plot()
cfd.tabulate()










