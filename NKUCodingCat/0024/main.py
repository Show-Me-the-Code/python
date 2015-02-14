#coding=utf-8
const = """
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="utf-8">
    <style type="text/css">
        h1
        {
            color: green;
        }
        table, th, td
        {
            border: 1px solid blue;
        }
        table
        {
            border-collapse: collapse;
            width: 100%;
        }
        th
        {
            height: 50px;
        }
        td.task
        {
            width: 70%;
        }
        input#delete
        {
            font-size: 15px;
            color: blue;
            background-color: #FFFFFF;
            border-width: 0;
            cursor: pointer;
        }
        textarea
        {
            vertical-align: middle;
            width: 500px;
            height: 100px;
        }
        input#submit
        {
            width: 107px;
            height: 42px;
            border-width: 0;
            font-size: 17px;
            font-weight: 500;
            border-radius: 6px;
            cursor: pointer;
        }
    </style>
</head>

<body>
<h1>TodoList应用演示</h1>

<form action="" method="post">

    <table>
        <tr>
            <td class="task_h"><div align="center">任务</div></td>
            <td class="manage_h"><div align="center">管理</div></td>
        </tr>
        <tr>
            <td class="task">{{ task.task }}</td>
            <td class="manage">
              <div align="center">
                <input type="submit" name="id-1" id="delete" value="删除" />
              </div></td>
        </tr>
		<tr>
            <td class="task">{{ task.task }}</td>
            <td class="manage">
              <div align="center">
                <input type="submit" name="id-2" id="delete" value="删除" />
              </div></td>
        </tr>
    </table>
    <br>
    <textarea name="newtask" id="newtask" maxlength="500"></textarea>
    <input type="submit" name="new" id="submit" value="创建新任务" />
</form>


</body>
</html>
"""


from bottle import static_file,route, run, post, request, redirect
import os,  urllib,re,json,time
Root = os.path.split(os.path.realpath(__file__))[0]+"/static/"


@route('/todo')
def index():
	return const
@post('/todo')
def Accept():
	Req = request.body.read()
	L = re.split("&",Req)
	M = {}
	for i in L:
		A = re.split("=",i)
		M[A[0]] = urllib.unquote(A[1])
	return json.dumps(M)
run(host='localhost',port=8080)