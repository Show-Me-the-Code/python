#coding=utf-8
const = """
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="utf-8">
<link type="text/css" rel="stylesheet" href="./static/css.css" />
</head>

<body>
<h1>TodoList应用演示</h1>

<form action="" method="post">

    <table>
        <tr>
            <td class="task_h"><div align="center">任务</div></td>
            <td class="manage_h"><div align="center">管理</div></td>
        </tr>

		{0}
    </table>
    <br>
    <textarea name="newtask" id="newtask" maxlength="500"></textarea>
    <input type="submit" name="new" id="submit" value="创建新任务" />
</form>


</body>
</html>
"""


from bottle import static_file,route, run, post, request, redirect, error
import os,  urllib,re,json,time
Root = os.path.split(os.path.realpath(__file__))[0]+"/static/"
import SQLIO

@route('/todo')
def index():
	return const.format(SQLIO.PageMake(),)
@post('/todo')
def Accept():
	Req = request.body.read()
	L = re.split("&",Req)
	M = {}
	for i in L:
		A = re.split("=",i)
		M[A[0]] = urllib.unquote(A[1])
	for j in M.keys():
		if re.findall("id-",j):
			SQLIO.SQL_del(int(j[3:]))
			redirect('/todo', 302)
	try:
		type = M["new"]
		newtask = M["newtask"]
	except:
		redirect('/error', 404)
	if newtask != "":
		SQLIO.SQL_in(newtask)
		redirect('/todo', 302)
	else:
		return "=.=所以你想添加什么任务呀"
	
@route('/error')
def err():
	return "虽然不知道你在干什么但是触发了服务器错误呢"
@route('/static/<filename>') 
def server_static(filename):
	return static_file(filename, root=Root)
run(host='localhost',port=8080)