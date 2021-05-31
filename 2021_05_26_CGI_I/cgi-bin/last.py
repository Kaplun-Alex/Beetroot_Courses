#!C:\Program Files\Python39\python.exe
import sqlite3 as sq
con = sq.connect('E:/Python_Projects/Beetroot_Courses_Homework/2021_05_26_CGI/cgi-bin/places.sqlite')
cur = con.cursor()
print("Content-type: text/html")
print()
print()

def executor(point):
    print('<!DOCTYPE html><html class="client-nojs" lang="ru" dir="ltr"><head><meta charset="UTF-8"></head><html><body><h2>Report</h2>')
    cur.execute(point)
    con.commit()
    c = cur.fetchall()
    for i in c:
        print(f"<li>{i[2]} - <a href={i[0]}> {i[0]} </a></li>")
    print('</body></html>')


executor("select url, title, datetime(h.visit_date/1000000, 'unixepoch') from moz_historyvisits h inner join moz_places p on h.place_id = p.id")

