#coding=utf-8
from __future__ import print_function

import os
import sys
import string
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from sklearn import metrics

from sklearn.cluster import KMeans, MiniBatchKMeans

import logging
from optparse import OptionParser
import sys
from time import time

import numpy as np

reload(sys)
sys.setdefaultencoding('utf8')

op = OptionParser()
op.add_option("--lsa",
              dest="n_components", type="int",
              help="Preprocess documents with latent semantic analysis.")
op.add_option("--no-minibatch",
              action="store_false", dest="minibatch", default=True,
              help="Use ordinary k-means algorithm (in batch mode).")
op.add_option("--no-idf",
              action="store_false", dest="use_idf", default=True,
              help="Disable Inverse Document Frequency feature weighting.")
op.add_option("--use-hashing",
              action="store_true", default=False,
              help="Use a hashing feature vectorizer")
op.add_option("--n-features", type=int, default=10000,
              help="Maximum number of features (dimensions)"
                   " to extract from text.")
op.add_option("--verbose",
              action="store_true", dest="verbose", default=False,
              help="Print progress reports inside k-means algorithm.")

path = './user_data/'
filelist = os.listdir(path)
corpus = []  #存取100份文档的分词结果，其格式类似于:
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

#vectorizer = CountVectorizer()
t_vectorizer = TfidfVectorizer()
#fit = vectorizer.fit_transform(corpus)#生成出现几次的向量
tfidf = t_vectorizer.fit_transform(corpus)
print("n_samples: %d, n_features: %d" % tfidf.shape)

#word = vectorizer.get_feature_names() #所有文本的关键字
#weight = tfidf.toarray()             #对应的tfidf矩阵

c_num = 5#聚类数目

km = KMeans(n_clusters=c_num, init='k-means++', max_iter=100, n_init=4)
km.fit(tfidf)


order_centroids = km.cluster_centers_.argsort()[:, ::-1]
terms = t_vectorizer.get_feature_names()
for i in range(c_num):
    print("Cluster %d:" % i, end='')
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind], end='')
    print()

l = km.labels_
f = open('kmeans.log', 'w')
for i in range(len(users)):
    print(users[i], l[i], file=f)
