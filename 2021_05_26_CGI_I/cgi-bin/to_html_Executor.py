#!C:\Program Files\Python39\python.exe
import sqlite3 as sq

con = sq.connect('places.sqlite')
cur = con.cursor()
def executor(point, file=0, filename='Temp.txt'):
    head = '<!DOCTYPE html>\n<head>\n<meta charset="UTF-8">\n</head>\n<html>\n<body>\n<h2>Report</h2>\n'
    legs = '</body>\n</html>\n'
    cur.execute(point)
    con.commit()
    c = cur.fetchall()
    print(c)
    if file != 0:
        f = open(filename, 'a')
        f.write(head)
        for i in c:
            f.write(f"<li>{i[2]} - <a href={i[0]}> {i[0]} </a></li>\n")
        f.write(legs)
        f.close()
    return c

executor("select url, title, datetime(h.visit_date/1000000, 'unixepoch') "
         "from moz_historyvisits h inner join moz_places p on h.place_id = p.id", 1, 'Visits.html')


