# coding:utf-8
import MeCab
text = "菅直人首相は野党の出方や世論を見極めつつ判断する考えだ。"

with open("/Users/kaba/Desktop/a") as f:
    text = f.read()

tagger = MeCab.Tagger('-Ochasen')
tagger = MeCab.Tagger('-Owakati')


node = tagger.parseToNode(text)
keywords = {}


while node:

    if node.feature.split(",")[0] in ["名詞"]:
        if not node.surface in keywords.keys():
            keywords[node.surface] = 1
        else:
            keywords[node.surface] += 1
    node = node.next

for k, v in sorted(keywords.items(), key=lambda x: x[1]):
    if v > 3:
        print(k, v)
