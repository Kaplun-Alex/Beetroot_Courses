import sqlite3 as sq

con = sq.connect('places.sqlite')
cur = con.cursor()
def executor(point, file=0, filename='Temp.txt'):
    cur.execute(point)
    con.commit()
    c = cur.fetchall()
    print(c)
    if file != 0:
        f = open(filename, 'w', encoding="utf-8")
        f.write(str(c))
        f.close()
    return c
executor("select url, title, datetime(h.visit_date/1000000, 'unixepoch') "
         "from moz_historyvisits h inner join moz_places p on h.place_id = p.id", 1, 'Visits.txt')
time = str(executor("select (max(moz_historyvisits.visit_date)-min(moz_historyvisits.visit_date))/1000000 "
                "from moz_historyvisits", 0, 'time_of_visits.txt'))
int_time = int(time[2:-3])
print(f'time -  {int_time} sec')