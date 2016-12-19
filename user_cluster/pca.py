#coding=utf8
import sys
import os
import matplotlib
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD, PCA

reload(sys)
sys.setdefaultencoding('utf8')

matplotlib.use('Agg')

path = './user_data/'
filelist = os.listdir(path)
corpus = []  #取文档的分词结果:
users = []
for ff in filelist :
    num, _ = ff.split('.')
    num = int(num)
    users.append(num)
    fname = path + ff
    f = open(fname,'r+')
    content = f.read()
    f.close()
    corpus.append(content)

vectorizer = CountVectorizer()
fit = vectorizer.fit_transform(corpus)

X = TruncatedSVD(n_components=2).fit_transform(fit)
#X = PCA(n_components=2).fit_transform(fit)

plt.scatter(X[:, 0], X[:, 1], s=40, c='gray')
plt.savefig('pca.jpg')