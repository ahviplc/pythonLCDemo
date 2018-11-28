# _*_ coding: utf-8 _*_

"""
python_markov_chain.py

Version: 0.1
Author: LC
DateTime: 2018年11月28日11:17:24
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
           http://oneplusone.vip/index.html

"""

import nltk
import random


file = open('Text/Walden.txt', 'r')
walden = file.read()
walden = walden.split()


def makePairs(arr):
    pairs = []
    for i in range(len(arr)):
        if i < len(arr) - 1:
            temp = (arr[i], arr[i + 1])
            pairs.append(temp)
    return pairs


def generate(cfd, word='the', num=500):
    for i in range(num):
        # make an array with the words shown by proper count
        arr = []
        for j in cfd[word]:
            for k in range(cfd[word][j]):
                arr.append(j)
        print(word, end=' ')

        # choose the word randomly from the conditional distribution
        word = arr[int((len(arr)) * random.random())]

pairs = makePairs(walden)
cfd = nltk.ConditionalFreqDist(pairs)
generate(cfd)
