# coding:utf-8
import codecs
import html2text
from glob import glob
 
s=""

for fileName in glob(""):
    print fileName
    with codecs.open(fileName, "r", "shift-jis") as f:
        # print f.read()
        s+=html2text.html2text(f.read())
f = open("text", "w")
f.write(s)
f.close()
