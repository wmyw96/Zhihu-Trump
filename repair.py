# f = open("questions2.csv","r")
# for line in f.readlines():
# 	count = 0
# 	for i in range(0,len(line)):
# 		if (line[i] == "\""):
# 			count += 1
# 		if (line[i] == ","):
# 			if (count % 2 == 1):
# 				line[i] = "，"
# 				
f = open("questions.csv","r")
gg = open("hhh.csv","w")
for line in f.readlines():
	nowline = line[0]
	for i in range(1,len(line)):
		if (line[i] == " " and line[i-1] == ","):
			continue
		else:
			nowline = nowline + line[i]
	gg.write(nowline)