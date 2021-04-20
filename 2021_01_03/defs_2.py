def square(sq):
    p = sq * 4
    s = sq ** 2
    d = 2**(1/2) * sq
    return p, s, d


#inp = int(input('Сторона квадрату? - '))
#print(square(inp))


def season(sz):     # Посчитал сто хранить словарь выгоднее чем перебирать диапазоны
    ds = {'1': 'Зимиа', '2': 'Зимиа', '3': 'Весна', '4': 'Весна', '5': 'Весна', '6': 'Лето', '7': 'Лето',
          '8': 'Лето', '9': 'Осень', '10': 'Осень', '11': 'Осень', '12': 'Зима'}
    rez = ds[sz]
    return rez


#inps = input('Порядковий номер місяця - ')
#print(season(inps))


def dice():
    import random
    rn = random.Random()
    fst = rn.randint(1, 6)
    scd = rn.randint(1, 6)
    return fst, scd


def run_dice():
    count = ''
    while count == '':
        count = input('Бросить кубики - Enter/Выход - 0: ')
        if count == '':
            res = dice()
            print(res)
        else:
            print('GAME OVER')
            break


#run_dice()


def graph_dice():
    dice_dict = {1: '⚀', 2: '⚁', 3: '⚂', 4: '⚃', 5: '⚄', 6: '⚅'}
    import random
    rn = random.Random()
    fst = rn.randint(1, 6)
    scd = rn.randint(1, 6)
    gfst = dice_dict[fst]
    gscd = dice_dict[scd]
    return gfst, gscd


def graph_run_dice():
    count = ''
    while count == '':
        count = input('Бросить кубики - Enter/Выход - 0: ')
        if count == '':
            res = graph_dice()
            print(res)
        else:
            print('GAME OVER')
            break
'''????????
>>>print('⚀'.encode('utf-8'))
b'\xe2\x9a\x80'
>>>b'\xe2\x9a\x80'.decode('utf-8')
'⚀'
'''

#graph_run_dice()


def universal_dice(facets):
    import random
    rn = random.Random()
    fst = rn.randint(1, facets)
    scd = rn.randint(1, facets)
    return fst, scd


def universal_run_dice():
    count = ''
    while count == '':
        fc = int(input('Кількість граней? - '))
        count = input('Бросить кубики - Enter/Выход - 0: ')
        if count == '':
            res = universal_dice(fc)
            print(res)
        else:
            print('GAME OVER')
            break


#universal_run_dice()


def vedro_kubov(facets, kk):
    import random
    count = kk
    sps = []
    while True:
        if count != 0:
            rn = random.Random()
            fst = rn.randint(1, facets)
            count -= 1
            sps.append(fst)
        else:
            break
    return sps


def run_vedro_kubov():
    count = ''
    while count == '':
        count = input('Бросить кубики - Enter/Выход - 0: ')
        if count == '':
            fc = int(input('Кількість граней? - '))
            kk = int(input('Кількість кубіків? - '))
            res = vedro_kubov(fc, kk)
            print(res)
        else:
            print('GAME OVER')
            break


#run_vedro_kubov()
