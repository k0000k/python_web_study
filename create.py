#!C:\Users\admin\AppData\Local\Programs\Python\Python310\python.exe
print("content-type:text/html; charset=UTF-8\n")

import cgi, os
import view

form = cgi.FieldStorage()

if 'id' in form:
    pageId = form["id"].value
    description=open('data/'+pageId,'r').read()

else:
    pageId = 'Welcome'
    description='Hello Web'

print('''<!doctype html>
<html>
<head>
  <title>WEB - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {lists}
  </ol>
  <a href="create.py">create</a>
  <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
      <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description,lists=view.getList()))
