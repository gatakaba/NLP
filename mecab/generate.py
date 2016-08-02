#coding:utf-8
import sys 
import urllib
import MeCab
import random
import re
 
def wakati(text):
    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    
    result = m.rstrip(" \n").split(" ")
    return result
 
if __name__=="__main__":
    f = open("text", "r")
    src = f.read()
    #注：MeCabはunicode型だとパースしてくれない
    wordlist = wakati(src)
    markov = {}
    w1, w2, w3 = '', '', ''
    for word in wordlist:
        if w1 and w2 and w3:
            if (w1,w2,w3) not in markov:
                markov[(w1,w2,w3)] = []
            markov[(w1,w2,w3)].append(word)
        w1,w2,w3=w2,w3,word
    sentence=''
    w1,w2,w3=random.choice(markov.keys())
    #カウントの数はおこのみで
    cnt = 0
    for i in range(100):
        if markov.has_key((w1,w2,w3))==True:
            tmp = random.choice(markov[(w1,w2,w3)])
            sentence += tmp
            cnt += 1
        w1, w2, w3 = w2, w3, tmp
    print cnt
    #時々、文の切れっ端から最初の文章が始まるので、最初の句点(。)までの部分は取っ払う。 
    sentence = re.sub("^.+?。", "", sentence)
    #閉じ括弧も同様
    sentence = re.sub("^」", "", sentence)       
    #あと、最後の句点(。)から先も取っ払ってしまう
    sentence = re.search(r".+。", sentence).group()
    
    print(sentence).split("。")[0] + "。" + (sentence).split("。")[1] + "。"
    print(len(sentence))
    