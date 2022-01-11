import os
import html_sanitizer

def getList():
    sanitizer=html_sanitizer.Sanitizer()
    files=os.listdir('data')
    lists=''
    for i in files:
        i=sanitizer.sanitize(i)
        lists=lists+'<li><a href="index.py?id={name}">{name}</a></li>'.format(name=i)
    return lists
