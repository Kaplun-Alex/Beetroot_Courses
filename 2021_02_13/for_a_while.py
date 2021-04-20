#Все зроблено через Def щоб не мудохаться з чистим злом - глобальними змінними.

def firstwhileex():
    print('Завдання 1 через while')
    s = 0
    ls = []
    while s < 10:
        ls.append(s)
        s += 1
    print(ls)
    ls.reverse()
    print(ls)

def firstforex():
    print('Завдання 1 через for')
    ls = []
    for i in range(10):
        ls.append(i)
    print(ls)
    ls.reverse()
    print(ls)


def secondwhileex():
    print('Завдання 2 через while')
    s = 0
    ls = []
    while s <= 1000:
        ls.append(s**2)
        s += 1
    print(ls)


def secondforex():
    print('Завдання 2 через for')
    ls = []
    for i in range(1000):
        ls.append(i**2)
    print(ls)


def thirdwhileex():
    print('Завдання 3 через while, тупа сумма')
    ls = []
    s = 0
    appossum = 0
    while s < 1000:
        ls.append(s)
        appossum += ls[-1]
        s += 1
    mid = appossum/len(ls)
    print(ls)
    print(appossum)
    print(mid)


def thirdforex():
    print('Завдання 3 через for, елементарна сумма')
    ls = []
    for i in range(1000):
        ls.append(i)
    mid = sum(ls)/len(ls)
    print(ls)
    print(mid)


def inputqwhile():
    print('Завдання 4 через while True, спонукало вже трохи помудохаться.')
    print("Додай свої справи, в кінці введи  - 'q'")
    ls = []
    while True:
        job = input()
        if job == 'q':
            print('Всі твої справи  \n', ls)
            break
        else:
            ls.append(job)
            print('Додай наступну братюня!')


def perebor():
    print('Завдання 5(4+ перевірка)')
    print("Додай свої справи, в кінці введи  - 'q'")
    ls = []
    while True:
        job = input()
        if job == 'q':
            print('Всі твої справи  \n', ls)
            break
        else:
            ls.append(job)
            print('Додай наступну братюня!')

    pereborlist = []

    for i in ls:
        if i.islower() is True:
            pereborlist.append(i)

    print(pereborlist)


perebor()
