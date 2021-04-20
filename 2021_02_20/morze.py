'''
1. Напишите скрипт, который бы получал на вход фразу
и переводил бы ее в азбуку Морзе в виде разделенных
пробелам точек и тире.
'''


def firstex():
    f = open('morze.txt', 'r', encoding='utf8')
    t = f.readlines()
    f.close()
    morze_dict = {}
    for i in t:
        morze_dict[i[0]] = i[2:-1]
    print(t)
    print(len(t))
    print(morze_dict)
    print(len(morze_dict))
    fraza = input('Напиши фразу: ').upper()
    rez = []
    for i in fraza:
        rez.append(morze_dict[i])
    out = ' '.join(rez)
    print(fraza)
    print(out)


'''
Напишите скрипт, который бы выполнял 
обратное действие - получал на вход точки-тире,
разделенные пробелами и переводил бы их в текст
'''


def secondex():
    f = open('morze.txt', 'r', encoding='utf8')
    t = f.readlines()
    f.close()
    morze_dict = {}
    reverse_morze = {}
    for i in t:
        morze_dict[i[0]] = i[2:-1]
        reverse_morze[i[2:-1]] = i[0]
    print(morze_dict, len(morze_dict))
    print(reverse_morze, len(reverse_morze))
    f = open('dots_lines.txt', 'r', encoding='utf8')
    t = (f.readline()).split(' ')
    f.close()
    print(t)
    rez = []
    for i in t:
        rez.append(reverse_morze[i])
    print(''.join(rez))


'''
Взять за образец мой скрипт по работе с файлом с именами
 и профессиями и т.д. и модифицировать его так, чтобы он
читал первую строчку файла (где перечислены поля данных: 
ФИО, год рождения, и т.д.), делал из нее словарь и по нему
 последовательно запрашивал пользователя информацию о новом 
 сотруднике (в формате: "фио?", ...), а потом добавлял эту 
 информацию в исходный файл.
'''


def thirdex():
    f = open('Input_data_tuple_file.txt', 'r', encoding='utf8')
    t = (f.readline()).replace('\n', '')
    f.close()
    head = t.split(', ')
    print(head)
    head_dict = {}
    for i in range(len(head)):
        for j in head:
            head_dict[i] = head[i]

    while True:
        if input('Додати користувача? Так - 1/Ні - 0: ') == str('1'):
            user = []
            for i in head_dict:
                create = input('Введи ' + head_dict[i] + ': ')
                user.append(create + ', ')
            print(user)
            f = open('Input_data_tuple_file.txt', 'a', encoding='utf8')
            f.writelines(user)
            f.write('\n')
            f.close()
        else:
            print('До зустрічі братуха')
            break


'''
Сделать аналогичный скрипт для магазина - запрос данных по новому товару - и занесение его в csv-файл.
'''


def fourex():
    f = open('cmpl_Copy.csv', 'r', encoding='utf8')
    t = (f.readline()).replace('\n', '')
    f.close()
    print(t)
    head = t.split(' ; ')
    print(head)
    head_dict = {}
    for i in range(len(head)):
        for j in head:
            head_dict[i] = head[i]
    print(head_dict)

    while True:
        if input('Додати товар? Так - 1/Ні - 0: ') == str('1'):
            tovar = []
            for i in head_dict:
                create = input('Введи ' + head_dict[i] + ': ')
                tovar.append(create)
            print(tovar)
            tov_zpdv = int(tovar[-1])*1.2
            str_tov = ' ; '
            str_tov = str_tov.join(tovar) + ' ; ' + str(tov_zpdv) + ';'
            print(str_tov)
            f = open('cmpl_Copy.csv', 'a', encoding='utf8')
            f.writelines(str_tov)
            f.write('\n')
            f.close()
        else:
            print('До зустрічі братуха')
            break


def crutch():
    f = open('t9_dict.txt', 'r', encoding='utf8')
    t = f.readlines()
    f.close()
    t = [i.rstrip() for i in t]
    t[-1] = '0 -  '
    t9_dict = {}
    print(t)
    for i in t:
        try:
            t9_dict[i[0]] = i[4]
            t9_dict[i[0]*2] = i[5]
            t9_dict[i[0]*3] = i[6]
            t9_dict[i[0]*4] = i[7]
            t9_dict[i[0]*5] = i[8]
        except IndexError:
            pass
    print(len(t9_dict))
    print(t9_dict)
    vvod = input('Хэрач цыфры братюня: ')
    for i in range(0, 10):
        gen = [5, 4, 3, 2, 1]
        for j in gen:
            try:
                key = str(t9_dict[str(i)*j])
                find_obj = str(str(i) * j)
                zamena = vvod.replace(find_obj, key)
                vvod = zamena
#                print(find_obj)
#                print(key)
#                print(vvod)
#                print(zamena)
            except KeyError:
                pass
    print(vvod)

crutch()
