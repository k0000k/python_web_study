#!C:\Users\admin\AppData\Local\Programs\Python\Python310\python.exe

import cgi, os

form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove("data/"+pageId)

print("Location: index.py")
print()
