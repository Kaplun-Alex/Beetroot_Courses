import os
import datetime

dt = str(datetime.datetime.today())


def file():
    os.open('log.txt', os.O_RDWR | os.O_CREAT)
    f = open('log.txt', 'a')
    f.write('Program run ' + dt + '\n')
    f.close()


file()


def logappend(l):
    f = open('log.txt', 'a')
    f.write('Справа '+l+'\n')
    f.close()


todo = []


print('Привіт братуха, маєш справи?')
print('Додай декілька нагальних справ')
todo.append(input())
logappend(todo[0])
for i in range(6):
    z = 6-i
    print('Наступна, зосталось ' + str(z))
    todo.append(input())
    logappend(todo[i+1])
    print('Додав')

print('Всі твої справи - ' + str(todo))
print('Перша справа - ' + todo[0] + '\n' +
      'Третя справа - ' + todo[2] + '\n' +
      'Четверта справа - ' + todo[3] + '\n' +
      'Остання справа - ' + todo[6] + '\n')
print('Пропоную тобі сьогодні виконати ' + '\n' +
      str(todo[:3]) + '\n' + 'завтра' + '\n' + str(todo[3:]))
print('Бабу хочеш вжарить?' + '\n' + '1 - так' + '\n' + '0 - ні')

jar = input()
print(jar)

if jar == '1':
    print('Норм, молодець!')
    todo.append('Хочу бабу!')
    logappend(todo[-1])
else:
    print('Жаль, в карантин скидки!')
    todo.append('Підлічить потенцію')
    logappend(todo[-1])

print('Підсумуєм' + '\n' + str(todo))
todo[-1], todo[0] = todo[0], todo[-1]
print('Але я б змінив ' + '\n' + str(todo) + '\n')

print('END')


