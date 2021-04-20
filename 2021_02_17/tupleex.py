def firstex():
    print(t)
    for i in t:
        tup = tuple(i.split(','))
        print(tup)
        if tup[1] == ' м':
            f = open('male.txt', 'a')
            f.writelines('Кобєль пративный - ' + tup[0] + '\n')
            f.close()
            print('Кобєль пративный - ' + tup[0])
        elif tup[1] == ' ж':
            f = open('female.txt', 'a')
            f.writelines('Царевна -  ' + tup[0] + '\n')
            f.close()
            print('Царевна - ' + tup[0])
        else:
            print('Error')
    f = open('tuple_file.txt', 'r', encoding='utf=8')
    t = f.readlines()
    f.close()



def secondex():
    ls = [(), (), ('a', 'b'), ('a', 'b', 'c')]
    check_list = []
    for i in ls:
        if len(i) != 0:
            check_list.append(i)
    print(check_list)


def first_csv():
    f = open('cmpl.csv', 'r', encoding='utf8')
    t = f.readlines()
    f.close()
    for i in t:
        addturple = tuple(i.split(';'))
        c = addturple[2]
        print(c)
        item = 'Тонер картридж'
        if c.find(item) != -1:     # Якщо ця діч не знаходить то вертає -1, якщо знаходить то вертаєіндекс останньоїбукви
            f = open('cartridge.csv', 'a', encoding='utf8')
            f.write(c + '\n')
            f.close()
            print('Value(item) is in')
        else:
            print('Value(item) is not')


def second_csv():
    f = open('cmpl.csv', 'r', encoding='utf8')
    t = f.readlines()
    f.close()
    rez_b = []
    for i in t:
        tup = tuple(i.split(';'))
        item = 'Бумага'
        b = tup[2]
        price = float(tup[4].replace(',', '.'))
        if b.find(item) != -1 and price <= 800:
            rez_b.append(b)
            print('Норм, берем! - ' + str(tup) + '\n' + str(price))
            f = open('berem_bumagu.csv', 'a', encoding='utf8')
            f.writelines('Норм, берем! - ' + str(tup) + '\n' + str(price) + '\n')
            f.close()
        elif b.find(item) != -1 and price > 800:
            print('Дорого! - ' + str(tup) + '\n' + str(price))
            f = open('ne_berem_bumagu.csv', 'a', encoding='utf8')
            f.writelines('Дорого! - ' + str(tup) + '\n' + str(price) + '\n')
            f.close()


second_csv()
