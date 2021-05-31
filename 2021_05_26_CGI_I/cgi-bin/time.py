import datetime
vrem = datetime.datetime.strftime(datetime.datetime.now(), "%Y.%m.%d %H:%M:%S")
# служебные заголовки
print("Content-type: text/html")
# содержимое сайта
print('''
<!DOCTYPE html>
<html class="client-nojs" lang="ru" dir="ltr">
<head>
<meta charset="UTF-8"/>
'</head>''')
print('<body>')
print('<title>Дата и время</title>')
print('<h1>Текущее время:</h1>')
print(f'<p>{vrem}</p>')
print('<a href="../index.html\n\n">MAIN_PAGE</a>')
print('</body>')
print('</html>')
