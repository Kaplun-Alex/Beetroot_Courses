import os


def find_files(f):
    files = os.listdir()
    for i in files:
        if i == f:
           ac = os.access('new.txt', os.F_OK)
           print('объект существует - ' + str(ac))
           ac = os.access('new.txt', os.R_OK)
           print('доступен на чтение - ' + str(ac))
           ac = os.access('new.txt', os.W_OK)
           print('доступен на запись - ' + str(ac))
           ac = os.access('new.txt', os.X_OK)
           print('доступен на исполнение - ' + str(ac))
        else:
            pass
    print(files)


#find_files('new.txt')


def find_file_in_dir(cat, file):
    catalog = []
    rez = 0
    address_rez = ''
    for i in os.walk(cat):
        catalog.append(i)
    print(catalog)
    for address, dirs, files in catalog:
        for f in files:
            if f == file:
                print('Файл тутво - ' + address + '/' + f)
                address_rez = address
                rez = 1
            else:
                pass
    if rez == 0:   # ну тут конечно гонево получается, если без этого то результат функции будет постоянно в else печаталь 'Нихера немаэ', а так двойная перепроверка.
        print('Нихера немаэ')
        address_rez = '0'

    return address_rez


#find_file_in_dir('C:\install', 'new.txt')


def pathhhh():
    pth = os.environ.copy() # опять этот метод без КОПИ дает обект класа а не возвращает словарь!!!!!! - ДИЧ!
    return pth


def check():
    rez = 0
    ka = os.getcwd()
    print(ka)
    root_list = list(root.values())
    print(root_list)
    for i in root:
        if ka == root_list:
            print('текущая папка есть в PATH')
            rez = 1
        else:
            pass
    if rez == 0:
        print('Текущей папки нет PATH')


#root = pathhhh()
#check()
