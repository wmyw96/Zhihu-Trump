#coding=utf-8

import os
import time
import sys
import string
import re
from zhihu_oauth import ZhihuClient

reload(sys)
sys.setdefaultencoding('utf8')

'''
f = open(sys.argv[1], 'r')
user_dict = {}
for line in f.readlines():
    tokens = line.strip().split('\001')
    uid, support = int(tokens[6]), tokens[9]
    if support == 'Trump'
'''

TOKEN_FILE = 'token.pkl'

client = ZhihuClient()

if os.path.isfile(TOKEN_FILE):
    client.load_token(TOKEN_FILE)
else:
    client.login_in_terminal()
    client.save_token(TOKEN_FILE)

quId = raw_input('questionId: ')
quList = [quId]

for quId in quList:
    question = client.question(int(quId))
    #output.write('quId\001content\001author\001voteup_count\001thanks_count\001comment_count\001id\001created_time\001updated_time\001support\001who_win\n')

    for answer in question.answers:
        id = answer.id
        author = answer.author
        if author.over:
            continue
        if author.following_topics:
            topics = ['_'.join(x.name.split(' ')) for x in author.following_topics]
            output = open('user_data/'+str(id)+'.txt', 'w')
            output.write(' '.join(topics))
            output.close()