import lms_os_task as l     #імпорт функцій визначення кількості символів та строк в шуканому файлі.
import os_praktice  #імпорт файлу з функціями по пошуку і перебору вказаних файлів

file_finder = input("Введи ім'я файлу що шукаєш з вказаним розширенням - ")
finder_root = input("Введи директорію пошуку файлу що шукаєш в форматі E:/Python Projects... - ")


def all_off():   # Тут доречі жорстокий косяк з коренем E:\ -> E:/ то таке необхідно кумекать)))
    catalog_rez = os_praktice.find_file_in_dir(finder_root, file_finder)    # пошук працюэ просто зачекай, дохрена файлов какбе..
    print(catalog_rez)   # отримали результат виконання функції пошуку(return address_rez) з імпортовапного модулю os_practice
    file_param = ''
    if catalog_rez != '0':
        try:
            file_param = l.all_of(catalog_rez+'/'+file_finder)   # отримали кортеж з функції all_of імпортованого модулю lms_of-task
        except UnicodeError:
            print('Формат не .txt або сталася геть невідома хрінь!')
    else:
        print('Файл відсутній')
    print(file_param)


'''
Для початку взяли модуль lms_os_task та модуль os_praktice
lms_os_task визначає кількість символів та строк у файлі.
os_praktice вигрібає усі директорії та файли в операційній системі, шукає в ній файл що задали для пошуку
повертає шлях до цього файлу в форматі E:/Python Projects в змінну catalog_rez строкового типу, потім передаєм
цюзмінну в файл lms_os_task де отримуєм параметри файлу задані в завдвнні.
Косяків вагон! Прога шукає тільки те що в адекваті можна перечитать в UTF8/txt
Код виконаний в рамках завдання.
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb3 in position 10: invalid start byte - .gif
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xdb in position 2349: invalid continuation byte - .torent
Відсутність файлу працює і виводить що файлу немає. Але маєм ще невідомі ексепшини відповідно бо ексепшини ще треба описувать, 
ну влом короче.
'''

# E:/ - прохання ще раз пояснить!
all_off()
