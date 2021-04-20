def firstex():
    rep = ',.()!?'
    f = open('Fenomen.txt', 'r', encoding='utf8')
    t = f.read().lower()
    f.close()
    t = t.replace('\n', ' ')
    for i in rep:
        t = t.replace(i, '')
    sp = t.split(' ')
    print(sp)
    unique = {}
    for i in sp:
        unique[i] = sp.count(i)
    unique.pop('')
    print(unique)


stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
dich = []
summ = 0


def secondex():
    dich = []
    res = 0
    its = list(stock.values()) # values()	Returns a list of all the values in the dictionary (Пиздеж! <class 'dict_values'>)
    print(type(its))
    itp = list(prices.values())
    print(itp, its)
    for i in range(0, len(its)):
        dich.append(itp[i]*its[i])
        res += (itp[i]*its[i])
    print(dich, res)


secondex()
