#-*- coding: UTF-8 -*- 

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import jieba
from django.shortcuts import render
import re
import datetime
from datetime import datetime
import os
import time
import sys
text = """
<head>%s
	<link rel="stylesheet" href="../../static/styles.css">
	<link rel="stylesheet" href="../../static/button.css">
	<link rel="stylesheet" href="../../static/responsive-nav.css">
	<link rel="stylesheet" href="../../static/hhh.css">
	<script src="../../static/responsive-nav.js"></script>
	<script type="text/javascript" src="../../static/jquery.min.js"></script>
	<script language="JavaScript">
var timerID = null;
var timerRunning = false;
function stopclock (){
  if(timerRunning)
  clearTimeout(timerID);
  timerRunning = false;
}
function startclock () {
  stopclock();
  showtime();
}
function showtime () {
  var now = new Date();
  var hours = now.getHours();
  var minutes = now.getMinutes();
  var seconds = now.getSeconds();
  var timeValue = now.getYear()+1900+"年"+(now.getMonth()+1)+"月"+now.getDate()+"日" +((hours >= 12) ? " 下午 " : " 上午 " );
    timeValue += ((hours >12) ? hours -12 :hours);
    timeValue += ((minutes < 10) ? ":0" : ":") + minutes;
    timeValue += ((seconds < 10) ? ":0" : ":") + seconds;
  $('#time').html(timeValue);
  timerID = setTimeout("showtime()",1000);
  timerRunning = true;
}
$().ready(function(){
  startclock(); 
});
</script>

</head>
<div role="main" class="main">
      <div id="time" style="color:red;font-size:16px;"></div>
      <button id="changetime" class="button button-glow button-circle button-action button-jumbo">T</button>
<form class="form-inline" action="/mysite/search" method="post"> 
  搜索内容: <input type="text"  class="form-control" name="searchText" placeholder = "Search" value = "%s">
  <input type="submit" value="搜索" class="button button-pill button-primary" /></br>
 </form>
   <button id="changetext" class="button button-glow button-circle button-action button-jumbo">R</button> <br>
   %s
</div>

 <script type = "text/javascript">
 $("#changetime").bind("click",function(event){
 	$("#timeevents").toggle();});
 $("#changetext").bind("click",function(event){
 	$("#paragraph").toggle();});
 </script>
  """



hhh = dict()
print sys.path[0]
input = open(sys.path[0] + "/fenci.txt")
inputstr = input.read()
for element in inputstr.split('\001'):
	lists = element.split('!@#$%')
	hhh[lists[0].decode("utf-8")] = [x[0:10] for x in lists[1:]]
input.close()
@csrf_exempt
def deal(request):
	if request.method == "GET":
		return HttpResponse(text % ('<style> body{background-image:url("http://s.cn.bing.net/az/hprichbg/rb/YonneRiver_ZH-CN12864189829_1920x1080.jpg");}</style>',"",''))
	else:
		print request.POST
		starttime = datetime.now()
		searchContents = request.POST['searchText'].split(" ")

		html = ''
		count = 0
		os.system("rm -rf line")
		os.system("rm -rf density")
		os.system("mkdir line")
		os.system("mkdir density")
		current_file_path = sys.path[0]
		for searchContent in searchContents:
			print searchContent
			dates = set()
			tempoutput = open("density/" + searchContent + ".csv","w")
			for element in hhh[searchContent]:
				if (element[0:4] == "2015"):
					continue
				else:
					tempoutput.write(element + '\n')
			tempoutput.close()
			tempoutput = open("line/" + searchContent + ".csv","w")
			for element in hhh[searchContent]:
				if (element in dates):
					continue
				else:
					if (element[0:4] == "2015"):
						continue
					tempoutput.write(element + "," + str(hhh[searchContent].count(element)) + "\n")
					dates.add(element)
			tempoutput.close()
		tempoutput = open("temp.csv","w")
		for searchContent in searchContents:
			tempoutput.write("\"" + searchContent.encode("utf-8") + "\"" + "," + "\"" + current_file_path + "/line/" + searchContent.encode("utf-8") + ".csv" + "\"" + '\n')
			tempoutput.write("\"" + searchContent.encode("utf-8") + "\"" + "," + "\"" + current_file_path + "/density/" + searchContent.encode("utf-8") + ".csv" + "\"" + '\n')
		tempoutput.close()
		os.system("Rscript web.R")
		html += "<p>Line Plot</p>"
		if (len(searchContents) == 1):
			html += "<p>" + searchContents[0] + "</p><br>"
		else:
			html += "<p>" + searchContents[0] + "(R) vs " +searchContents[1] + "(B)</p><br>"
		html += '<img src="/static/myplot_line.jpg" height = "600" width = "600"/><br>'
		html += "<p>Density Plot</p>"
		if (len(searchContents) == 1):
			html += "<p>" + searchContents[0] + "</p><br>"
		else:
			html += "<p>" + searchContents[0] + "(B) vs " +searchContents[1] + "(G)</p><br>"
		html += '<img src="/static/myplot_density.jpg" height = "600" width = "600"/>'
		endtime = datetime.now()
		print starttime
		print endtime
		return HttpResponse(text.decode("utf-8") % (''," ".join(searchContents),html))

def get_current_files(path):
	current_file = os.listdir(path)
	all_files = []
	for file_name in current_file:
		all_files.append(file_name)
	return all_files

