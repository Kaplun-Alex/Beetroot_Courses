import sqlite3 as sq

con = sq.connect('places.sqlite')
cur = con.cursor()


def executor(point, file=0, filename='Temp.txt'):
    head = '<!DOCTYPE html>\n' \
           '<html>\n' \
           '<head>\n' \
           '<meta charset="UTF-8">\n' \
           '<style>\n' \
           'table {\n' \
           'font-family: arial, sans-serif;\n' \
           'border-collapse: collapse;\n' \
           'width: 100%;\n' \
           '}\n' \
           'td, th {\n' \
           'border: 1px solid #dddddd;\n' \
           'text-align: left;\n' \
           'padding: 8px;}\n' \
           'tr:nth-child(even) {\n' \
           'background-color: #dddddd;\n' \
           '}\n' \
           '</style>\n' \
           '</head>\n' \
           '<body>\n' \
           '<h2>Report Table</h2>\n' \
           '<table>\n' \
           '<tr>\n' \
           '<th>TIME</th>\n' \
           '<th>LINC</th>\n' \
           '</tr>\n'
    legs = '</table>\n' \
           '</body>\n' \
           '</html>\n'
    cur.execute(point)
    con.commit()
    c = cur.fetchall()
    print(c)
    if file != 0:
        f = open(filename, 'a')
        f.write(head)
        for i in c:
            f.write(f"<tr>\n <th>{i[2]}</th>\n <th><a href={i[0]}> {i[0]} </a></th>\n </tr>\n")
        f.write(legs)
        f.close()
    return c


executor("select url, title, datetime(h.visit_date/1000000, 'unixepoch') "
         "from moz_historyvisits h inner join moz_places p on h.place_id = p.id", 1, 'Visit_Table.html')
