# -*- coding: utf-8 -*-
# from HTMLParser import HTMLParser
import os
import jieba

# def get_current_files(path):
# 	current_file = os.listdir(path)
# 	all_files = []
# 	for file_name in current_file:
# 		all_files.append(file_name)
# 	return all_files

# class MYHTMLParser(HTMLParser):

# 	def handle_starttag(self, tag, attrs):
# 		global woshishabi
# 		if (tag == "article" or tag == "title"):
# 			woshishabi = False

# 	def handle_data(self, data):
# 		global woshishabi
# 		global out
# 		if (not woshishabi):
# 			out.write(data)

# 	def handle_endtag(self, tag):
# 		global woshishabi
# 		if (tag == "article" or tag == "title"):
# 			woshishabi = True

totalWords = set()
wordsMapping = dict()
f = open("no_mark_answers.txt","r")
jieba.load_userdict("userdict.txt")
f.readline()
for line in f.readlines():
	words = line.split("\001")
	cutResult = jieba.cut_for_search(words[1])
	lists = "\001".join(cutResult)
	seg_list = lists.split("\001")
	for i in range(0,len(seg_list)):
		if (seg_list[i] in totalWords):
			wordsMapping[seg_list[i]].append(words[8][:-1])
		else:
			totalWords.add(seg_list[i])
			wordsMapping[seg_list[i]] = [words[8][:-1]]
f.close()
f = open("no_mark_answers_1000-10000.txt","r")
jieba.load_userdict("userdict.txt")
f.readline()
for line in f.readlines():
	words = line.split("\001")
	cutResult = jieba.cut_for_search(words[1])
	lists = "\001".join(cutResult)
	seg_list = lists.split("\001")
	for i in range(0,len(seg_list)):
		if (seg_list[i] in totalWords):
			wordsMapping[seg_list[i]].append(words[8][:-1])
		else:
			totalWords.add(seg_list[i])
			wordsMapping[seg_list[i]] = [words[8][:-1]]
f.close()
output = open("mysite/fenci.txt","w")
for words in totalWords:
	output.write(words + "!@#$%" + "!@#$%".join(wordsMapping[words]) + '\n' + '\001')
output.close()
# SUFFIX = "/Users/songshihong/Desktop/py/html/"
# all_files = get_current_files("/Users/songshihong/Desktop/py/html")
# d = {}
# count = 0
# for path in all_files:
# 	print count
# 	woshishabi = True
# 	parser = MYHTMLParser()
# 	html = open(SUFFIX + path)
# 	htmlstr = html.read()
# 	out = open("/Users/songshihong/Desktop/py/text/" + path[:-5] + '.txt','w')
# 	try:
# 		parser.feed(htmlstr)
# 	except:
# 		continue
# 	out.close()
# 	input = open("/Users/songshihong/Desktop/py/text/" + path[:-5] + '.txt')
# 	seg_list = jieba.cut_for_search(input.read())
# 	input.close()
# 	out = open("/Users/songshihong/Desktop/py/jieba/" + path[:-5] + '.txt','w')
# 	lists = "\n".join(seg_list)
# 	out.write(lists.encode("utf-8"))
# 	out.close()
# 	input = open("/Users/songshihong/Desktop/py/jieba/" + path[:-5] + '.txt')
# 	for line in input.readlines():
# 		d.setdefault(line,set()).add(path[:-5])
# 	input.close()
# 	count += 1
# out = open("/Users/songshihong/Desktop/py/data.txt","w")
# out.write("!@#$%".join(map(lambda k: (k if k[-1] == '\n' else k + '\n') + "%$#@!" + "mmd".join(d[k]), d)))
# # for k in d:
# # 	out.write(k)
# # 	out.write(" ".join(d[k]))
# # 	out.write("\n")
# out.close()



