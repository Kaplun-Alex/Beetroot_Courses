f = open('red_apple.log', 'r')
t = f.readlines()
r = open('red_aple_404.log', 'a')
for i in t:
    if i.find(' 404 ') >= 0:
        r.write(i)
r.close()
f.close()