# coding=utf-8
from __future__ import unicode_literals, print_function

import os
import time
import sys
import string
import re
from zhihu_oauth import ZhihuClient
reload(sys)
sys.setdefaultencoding('utf8')

TOKEN_FILE = 'token.pkl'

client = ZhihuClient()

if os.path.isfile(TOKEN_FILE):
    client.load_token(TOKEN_FILE)
else:
    client.login_in_terminal()
    client.save_token(TOKEN_FILE)

quId = raw_input('questionId: ')
output = open(quId+'.csv', 'w')
option_list = {'0':'None', '1':'Trump', '2':'Hillary'}
quList = [quId]
qu_tu = re.compile(r'<img.*?>')
qu_br = re.compile(r'<br>')
for quId in quList:
    question = client.question(int(quId))
    output.write('content\001author\001voteup_count\001thanks_count\001comment_count\001id\001created_time\001updated_time\001support\001who_win\n')

    for answer in question.answers:
        id = answer.id
        voteup_count = answer.voteup_count
        comment_count = answer.comment_count
        author = answer.author.name
        created_time = time.localtime(question.created_time)
        created_time_str = time.strftime('%Y-%m-%d %H:%M:%S', created_time)
        content = answer.content.strip()
        thanks_count = answer.thanks_count
        updated_time = time.localtime(question.updated_time)
        updated_time_str = time.strftime('%Y-%m-%d %H:%M:%S', updated_time)
        support = 0#
        who_win = 0#
        content = qu_tu.sub('',content)
        content = qu_br.sub('',content)
        print(content)
        while True:
            support = raw_input('support whom:(0:none 1:trump 2:hi):')
            who_win = raw_input('who win:(0:none 1:trump 2:hi):')
            if support in option_list.keys() and who_win in option_list.keys():
                print('ok')
                support = option_list[support]
                who_win = option_list[who_win]
                break
        nums = [voteup_count,thanks_count,comment_count,id]
        nums = [str(x) for x in nums]
        contents = [content, author]
        contents.extend(nums)
        contents.append(created_time_str)
        contents.append(updated_time_str)
        contents.append(support)
        contents.append(who_win)
        output.write('\001'.join(contents)+'\n')
