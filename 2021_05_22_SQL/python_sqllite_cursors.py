import sqlite3 as sq

con = sq.connect('chinook.db')
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

executor('select * from customers', 0)
executor("select FirstName, LastName from customers where Country = 'India' "
         "ORDER BY FirstName", 1, 'India.txt')
executor("select FirstName, LastName from customers where Country = 'Brazil' "
         "ORDER BY FirstName", 1, 'Brazil.txt')
executor("select CustomerId, FirstName, LastName from customers where Country in ('Brazil', 'India') ORDER BY CustomerId", 1, 'All_Customers_India_and_Brazil.txt')