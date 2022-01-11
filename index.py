#!C:\Users\admin\AppData\Local\Programs\Python\Python310\python.exe
print("content-type:text/html; charset=UTF-8\n")

import cgi, os
import view
import html_sanitizer

sanitizer=html_sanitizer.Sanitizer()
form = cgi.FieldStorage()

if 'id' in form:
    title= pageId = form["id"].value
    description=open('data/'+pageId,'r').read()
    title=sanitizer.sanitize(title)
    description=sanitizer.sanitize(description)
    update_link='<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action='''
            <form action="process_delete.py" method="post">
                <input type="hidden" name="pageId" value={}>
                <input type="submit" value="delete">
            </form>
        '''.format(pageId)

else:
    title= pageId = 'Welcome'
    description='Hello Web'
    update_link=''
    delete_action=''

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
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=title, desc=description, lists=view.getList(), update_link=update_link, delete_action=delete_action))
