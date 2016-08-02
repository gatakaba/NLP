# coding:utf-8
from gensim import corpora, models, similarities
import MeCab
import logging
# logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s', level = logging.INFO)

with open("text") as f:
    lines = f.read()
lines = lines.split()
texts = []
t = MeCab.Tagger("-Owakati")
for line in lines:
    texts.append(t.parse(line).split())
# 辞書の作成
dictionary = corpora.Dictionary(texts)
dictionary.save('deerwester.dict')  # store the dictionary, for future reference
# 単語IDとのマッピング関係
with open("map.txt", "w") as f:
    for word in dictionary.token2id.keys():
        f.write(unicode(word) + "," + str(dictionary.token2id[word]) + "\n")
# コーパス
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('deerwester.mm', corpus)  # store to disk, for later use

model = models.word2vec.Word2Vec(corpus2, size = 200)
print model.most_similar(positive = [u"歩き"], negative = [], topn = 1)


