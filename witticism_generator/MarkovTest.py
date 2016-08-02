# coding:utf-8
import numpy as np
import random
import string

def generateSentense():
    # make sentence
    wordList = []
    for i in range(100):
        word=""
        for j in range(10):
            word += random.choice(string.lowercase)
        wordList.append(word)
    return wordList

if __name__=="__main__":
    print generateSentense()