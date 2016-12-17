# coding=utf-8
from __future__ import unicode_literals, print_function

import sys
import os
import time
from zhihu_oauth import ZhihuClient

TOKEN_FILE = 'token.pkl'


client = ZhihuClient()

if os.path.isfile(TOKEN_FILE):
    client.load_token(TOKEN_FILE)
else:
    client.login_in_terminal()
    client.save_token(TOKEN_FILE)

reload(sys)
outFile = open('questions.csv', 'w')
sys.setdefaultencoding('utf8')

qFile = open("topic/all_questions_id", 'r')
quList = []
for line in qFile.readlines():
    id = line[0:8]
    quList.append(id)

print('totally %d questions in 3 topics' % len(quList))
quList = list(set(quList))
print('totally %d questions in 3 topics (after unique)' % len(quList))

limit_time = time.strptime('2016-11-08 23:59:59', '%Y-%m-%d %H:%M:%S')

tot = 0

for quId in quList:
    question = client.question(int(quId))
    created_time = question.created_time

    # Id
    id = int(quId)

    # title
    title = question.title

    # prob_comment_count
    prob_comment_count = question.comment_count

    # follower_count
    follower_count = question.follower_count

    # answer_count
    answer_count = question.answer_count

    # answer_total_voteup
    # answer_total_comment

    answer_total_voteup = 0
    answer_total_comment = 0
    for answer in question.answers:
        answer_total_voteup += answer.voteup_count
        answer_total_comment += answer.comment_count

    answer_mean_voteup = 0
    answer_mean_comment = 0

    if (answer_count > 0):
        # answer_mean_voteup
        answer_mean_voteup = (answer_total_voteup + 0.0) / answer_count

        # answer_mean_comment
        answer_mean_comment = (answer_total_comment + 0.0) / answer_count


    # created_time
    created_time = time.localtime(question.created_time)
    created_time_str = time.strftime('%Y-%m-%d %H:%M:%S', created_time)

    if created_time > limit_time:
        continue

    # updated_time
    updated_time = time.localtime(question.updated_time)
    updated_time_str = time.strftime('%Y-%m-%d %H:%M:%S', updated_time)

    # popularity
    popularity = answer_count + prob_comment_count + follower_count + \
                 answer_total_voteup + answer_total_comment

    topicTrump = False
    topicHillary = False
    topicElection = False

    for topic in question.topics:
        if topic.id == '20023724':
            topicTrump = True
        if topic.id == '20019119':
            topicElection = True
        if topic.id == '19664274':
            topicHillary = True

    '''print(id, title, answer_count, prob_comment_count,
          follower_count, answer_total_voteup,
          answer_total_comment, answer_mean_voteup,
          answer_mean_comment, created_time_str, updated_time_str,
          popularity, topicTrump, topicElection, topicHillary)'''

    outFile.write('"%d","%s","%d","%d","%d","%d","%d","%lf","%lf","%s","%s","%d","%s","%s","%s"\n'
                  % (id, title, answer_count, prob_comment_count, follower_count, answer_total_voteup, answer_total_comment,
                     answer_mean_voteup, answer_mean_comment, created_time_str, updated_time_str, popularity, str(topicTrump),
                     str(topicElection), str(topicHillary)))

    tot = tot + 1
    print('have already visited %d questions' % tot)

outFile.close()

