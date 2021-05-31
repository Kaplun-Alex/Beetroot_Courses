#!/usr/bin/env python3
import cgi
print("Content-type: text/html")
print()
form = cgi.FieldStorage()
print('HELLO WORLD!111')
print(form)
print(f"<p><b>{form.getfirst('alex')}</b></p>") # печатаем объект
cgi.print_environ_usage()
cgi.print_environ()
