# coding=utf-8

#from __future__ import print_function

from bs4 import BeautifulSoup
from util import get_content
import sys

def find_question_by_link(topic_url, outFile):
    content = get_content(topic_url,0)
    soup = BeautifulSoup(content, "html.parser")

    questions = soup.findAll('a',attrs={'class':'question_link'})

    tot = 0
    for question in questions:
        tem_text = question.get_text()
        tem_id = question.get('href')
        tem_id = tem_id.replace('/question/', '')
        outFile.write('%s : %s\n' % (tem_id, tem_text))
        tot = tot + 1

    return tot


def find_new_question_by_topic(link_id, count, outFile):
    print('starting scratch topic %s, totally %d pages' % (link_id, count))
    new_question_amount_total = 0
    k = 1
    for i in range(1, count):
        topic_url = 'http://www.zhihu.com/topic/' + link_id + '/questions?page=' + str(i)
        new_question_amount_one_page = find_question_by_link(topic_url, outFile)
        new_question_amount_total = new_question_amount_total + new_question_amount_one_page

        if (new_question_amount_total >= k * 100):
            print('-- already found %d questions till page %d' % (new_question_amount_total, i))
            k = k + 1

        #if new_question_amount_one_page <= 2:
        #    break

def search_all(topicset, outFile):
    for key in topicset.keys():
        find_new_question_by_topic(key, topicset[key], outFile)

if __name__ == '__main__':
    reload(sys)
    outFile = open('all_questions', 'w')
    sys.setdefaultencoding('utf8')
    search_all({'20023724': 322, '20019119': 403, '19664274': 150}, outFile)
