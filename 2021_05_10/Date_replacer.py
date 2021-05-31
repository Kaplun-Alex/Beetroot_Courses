f = open('red_apple.log', 'r')
t = f.readlines()
f.close()

MonthDict = {'/Jan/': '-01-', '/Feb/': '-02-', '/Mar/': '-03-', '/Apr/': '-04-', '/May/': '-05-',
             '/Jun/': '-06-', '/Jul/': '-07-', '/Aug/': '-08-', '/Sep/': '-09-', '/Oct/': '-10-',
             '/Nov/': '-11-', '/Dec/': '-12-'}
r = open('red_apple_ISO_8601.log', 'a')
for i in t:
    home = i.find('[')
    end = i.find(']')
    rez = i[home:end + 1].replace(':', 'T', 1)
    rez = rez.replace(' ', "", 1)
    rez_month = rez[3:8]
    rez = rez.replace(rez[3:8], MonthDict[rez[3:8]])
    rez = rez[:23]+':'+rez[23:]
    i = i.replace(i[home:end + 1], rez)
    r.write(i)
r.close()

