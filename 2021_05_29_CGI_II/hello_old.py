#!/usr/bin/env python3
import os
print("Content-type: text/html")
print()
print('''
<!DOCTYPE html>

<html>

<head>
<meta charset="UTF-8"/>
</head>

<body>
<html>''')
if os.environ['QUERY_STRING']:
    for p in os.environ['QUERY_STRING'].split('&'):
        print(p.split('='))
        print()

else:
    print("Запросов не поступало")
print('HELLO!')
for i in os.environ:
    print(f"<p><b>{i}</b><br>{os.environ[i]}</p>")
print('''</body></html>''')