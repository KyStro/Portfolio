#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:57:07 2020

Kyle Strokes
SL: Sean Current
ISTA 331 hw5
4/15/2020

Collaborator: Samantha Robbins

This module measures the cosine similarity of a list of filenames.
It prints out the filenames in a sparse matrix, with the intersection
of each filename being how similar the text in the file is.
"""

import string
import pandas as pd
import numpy as np
from sklearn.feature_extraction import stop_words
from nltk.stem import SnowballStemmer


'''
This function takes in two vectors in the form of dictionaries, v1, v2 and
returns the dot product of the common key/values in both
'''
def dot_product(v1, v2):
    s1 = set(v1)
    s2 = set(v2)
    inter = s1.intersection(s2)
    return sum([v1[key]*v2[key] for key in inter])

'''
This function reutrns the length or magnitude of a vector in the form of
a dictionary. It raises each value to the 2nd power and sums all the values
then returns the square root of that sum.
'''
def magnitude(d):
    return np.sqrt(sum([v**2 for v in d.values()]))


'''
This function takes two dictionary form vectors and returns the cosine
similarity between them by taking the dot product divided into the product
of both of vector's magnitudes
'''
def cosine_similarity(d1, d2):
    return dot_product(d1,d2) / (magnitude(d1) * magnitude(d2))

'''
This function takes a filename, opens it, and removes all occurences of "n't"
in the text. Removes all punctuation and digits from the text. Makes the text
lowercase. The text is then returned.
'''
def get_text(filename):
    file = open(filename)
    text = file.read()
    text = text.replace("n't", "")
    text = text.translate(str.maketrans('', '', string.punctuation+string.digits))
    text = text.lower()
    return text
    
'''
This function takes a filename, a list of stop words, and a stemmer. For each
word in the file the word is stemmed to its root and then checked if it is a 
stop word. If it is not, the word is added to a dictionary. If the word has been
seen before, its count is incremented.
'''
def vectorize(filename, stop_words, stemmer):
    text = get_text(filename)
    d = {}
    for word in text.split():
        word = stemmer.stem(word.strip())
        if word == '':
            continue
        if word in stop_words:
            continue
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d
        
'''
This function takes a list of dictionary word counts like above and returns a
new dictionary of all the keys in the dictionaries mappped to the numbers
of times they occur in all the other dictionaries.
'''
def get_doc_freqs(listo_vects):
    total ={}
    for d in listo_vects:
        for key in d.keys():
            if key not in total:
                total[key] = 1
            else:
                total[key] += 1
    return total


'''
This function takes a list of word count dictionaries and converts each
word count of a word to a weighted value in a way that less common words
hold more weight. The dictionaries in the list are changed in place.
'''
def tfidf(listo_vects):
    doc_freqs = get_doc_freqs(listo_vects)
    num_docs = len(listo_vects)
    scale = 100/num_docs
    if num_docs >= 100:
        scale = 1
    for k,v in doc_freqs.items():
        new = 1 + np.log2(scale * num_docs/v)
        doc_freqs[k] = new  
    for doc in listo_vects:
        for k,v in doc.items():
            if k in doc_freqs.keys():
                doc[k] *= doc_freqs[k]


'''
This function takes a list of filenames, each file is read and vectorized.
A dataframe is made then to compare each file on their cosine similarities
with each other. The dataframe is returned.
'''  
def get_similarity_matrix(listo_files, stopws, stemmer):
    df = pd.DataFrame(index=listo_files, columns=listo_files)
    listo_vects = []
    for file in listo_files:
        vect = vectorize(file, stopws, stemmer)
        listo_vects.append(vect)
    tfidf(listo_vects)
    for i in range(len(df)):
        j=i+1
        while j < len(df.iloc[i]):
            df.iloc[i,j] = cosine_similarity(listo_vects[i], listo_vects[j])
            df.iloc[j,i] = cosine_similarity(listo_vects[i], listo_vects[j])
            j += 1
        df.iloc[i,i] = 1
    return df

'''
Uses get similarity matrix to compute the similarity matrix
for the 
ve sample documents, 00001.txt, 00002.txt, etc.
'''
def main():
    lis = ['0000'+str(i)+'.txt' for i in range(6)]
    sw = list(stop_words.ENGLISH_STOP_WORDS) + ['did', 'gone', 'ca']
    print(get_similarity_matrix(lis, sw, stemmer=SnowballStemmer("english")))
    


    
    
    
    