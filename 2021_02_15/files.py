def firstex():
    f = open('fio.txt', 'a')
    f.write((input('Введи своє Прізвище: '))+' ')
    f.write((input("Iм'я: "))+' ')
    f.write((input('По батькові: '))+'\n')
    f.write((input("Введи дату народження: "))+'.')
    f.write((input('Місяць: '))+'.')
    f.write((input('Рік: '))+'\n')
    f.close()
    f = open('fio.txt', 'r')
    t = f.read()
    print('Твої дані:'+'\n' + str(t))
    f.close()


def secondex():
    f = open('fio.txt', 'r')
    t = f.read()
    f.close()
    temp1 = t.find(' ')+1
    temp2 = t.rfind(' ')
    name = t[temp1:temp2]
    y1 = t.rfind('.')+1
    year = 2021 - int(t[y1:])
    print('Добрий день ' + name + '!' + '\n' + 'Ваш вік ' + str(year) + ' років!')


def weather():
    f = open('weather.log', 'r', encoding='utf-8')
    t = f.readlines()
#    print(t)
    f.close()
    s = 0
    st_mon = []
    for i in t:
        if i.startswith('2016-10'):
            st_mon.append(i)
    print(st_mon)
    for i in st_mon:
        temp_txt = i.split()[2] # Повторно пояснить за сплит
#        print(temp_txt)
        temp_int = int(temp_txt.replace('°C,',''))
#       print(temp_int)
        s = s + temp_int
#        print(s)
    print(s / len(t))


def weather_from_site():
    f = open('daily_obs.log', 'r')
    t = f.readlines()
    f.close()
    for i in t:
        right_t = i.replace('\n','')
        print(right_t)
    b = 0
    for i in t:
        bar = float(i.split()[-5])
        b = b+bar
    print('Середнє чавлення в інчах: ' + str(b/len(t)))
    print('Середнє чавлення в мм: ' + str((b / len(t))*25.4))


weather_from_site()
