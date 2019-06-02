#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:32:50 2019
cs224_NLP_2019_Lab_2
@author: junchengzhu
"""
# import my own corpus #
import nltk

from nltk.corpus import PlaintextCorpusReader
corpus_root = '/Users/junchengzhu/Lecture/nlp2019/Lab/Lab2/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')

text = wordlists.words('PRINCE.txt')
# print(len(text))


# Stemmers 词干提取器 提取‘happy’上下文 #
porter = nltk.PorterStemmer()

# print([porter.stem(t) for t in text])
porteredText = [porter.stem(t) for t in text]
# print(porteredText)


class IndexedText(object):

    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
                                 for (i, word) in enumerate(text))

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = int(width/4)                # words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])
            ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
            rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
            print(ldisplay, rdisplay)

    def _stem(self, word):
        return self._stemmer.stem(word).lower()
    
    
    
content = IndexedText(porter, text)
result = content.concordance('happy')


# Regular Expressions 正则表达式分割 #
pattern = r'''(?x)    # set flag to allow verbose regexps
     ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
   | \w+(-\w+)*        # words with optional internal hyphens
   | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
   | \.\.\.            # ellipsis
   | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
'''
# nltk.regexp_tokenize(text, pattern)


# 除去词内元音
deleteWords = []
rule = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
for w in words_D:
    deleteWords.append(''.join(re.findall(rule, w)))
print(deleteWords)

# 正则表达式匹配
rule = re.compile(r'^[abc].*ing$')
resultWords = []
for w in words_D:
    m = re.match(rule, w)
    if m:
        resultWords.append(w)
print(resultWords)


# Search for word start with 'a' or 'b' or 'c' and endswith 'ing' #
# save the result to a .txt file #
output_file = open('output.txt', 'w')
    
for theWord in text:
    for startChar in ['a', 'b', 'c']:
        if(theWord.lower().startswith(startChar) and theWord.lower().endswith('ing')):
            print (theWord)
            output_file.write(theWord + "\n")
                

output_file.close()                
                
          
                
                