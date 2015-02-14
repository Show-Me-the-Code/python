#coding=utf-8
from bottle import static_file,route, run, post, request, redirect
import os, makeweb, urllib,re,json,time
Root = os.path.split(os.path.realpath(__file__))[0]+"/static/"
Const = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>无标题文档</title>
<link type="text/css" rel="stylesheet" href="./static/css.css" />

</head>

<body>
<div id="1">
  <form id="form1" name="form1" method="post" action="">
    <label>名字
    <input id="name" type="text" name="textfield" tabindex="0" />
    </label>
    <p>
      <label>评论
      <textarea name="textarea" tabindex="1" style="height: 89px; width: 350px;"></textarea>
      </label>
    </p>
    <p>
      <label>
      <input id="Submit" type="submit" name="Submit" value="提交" />
      </label>
    </p>
  </form>
</div>
<div>
	%s
</div>
</body>
</html>

"""
@route('/board')
def index():
	return Const%makeweb.Pack(makeweb.Stor_out())
@post('/board')
def Accept():
	Req = request.body.read()
	L = re.split("&",Req)
	M = {}
	for i in L:
		A = re.split("=",i)
		M[A[0]] = urllib.unquote(A[1])
	New = {}
	New["Name"] = M["textfield"]
	New["Content"] = M["textarea"]
	makeweb.Stor_in(New)
	redirect('/board', 302)

@route('/static/<filename>') 
def server_static(filename):
	return static_file(filename, root=Root)
run(host='localhost',port=8080)
