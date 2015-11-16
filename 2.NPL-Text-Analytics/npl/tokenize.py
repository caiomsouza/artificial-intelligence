# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:26:43 2015

@author: caiomsouza
"""


import nltk
sentence = """NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum."""
tokens = nltk.word_tokenize(sentence)

print "Token"

print tokens


tagged = nltk.pos_tag(tokens)
tagged[0:6]

print "Tagged"

print tagged


entities = nltk.chunk.ne_chunk(tagged)

print "Entities: "

print entities


from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()

