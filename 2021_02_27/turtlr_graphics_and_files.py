import turtle   # Ну кароче, у нас все сложно(Женский вариант)
                # Ой все!
question = input('From file - 1/manually - 0: ')    # Запрос на тип операції файл/з клави


def zamanuha():   # обробка запросу згідно запросу, визначення висоти цифр та введенои елементів
    inpt = []
    if question == '1':
        f = open('number_params.txt', 'r', encoding='utf8')
        ft = f.read()
        f.close()
        lt = ft.split(', ')
        print(lt)
        for s in lt[0]:
            inpt.append(s)
        print(inpt)
        sizer = int(lt[1])
    else:
        for j in (input('Введи 10 цифр братюня: ')):
            inpt.append(j)
        sizer = int(input('Розмір? - '))
        print(inpt)
    return inpt, sizer


ret = zamanuha()    # розпаковка кортежу результатів що видала функуія замануха
inp = ret[0]
size = ret[1]
print(ret)

    # функції малювальника


def zero():
    t.down()
    x = t.xcor()
    y = t.ycor()
    t.goto(x+size, y)
    t.goto(x+size, y+(2*size))
    t.goto(x, y+(2*size))
    t.goto(x, y)
    t.up()
    t.goto(x+(2*size), y)   ##


def one():
    t.up()
    x = t.xcor()
    y = t.ycor()
    t.goto(x, y+size)
    t.down()
    t.goto(x+size, y+(2*size))
    t.goto(x+size, y)
    t.up()
    t.goto(x+(2*size), y)


def two():
    t.up()
    x = t.xcor()
    y = t.ycor()
    t.goto(x, y+(2*size))
    t.down()
    t.goto(x+size, y+(2*size))
    t.goto(x+size, y+size)
    t.goto(x, y)
    t.goto(x+size, y)
    t.up()
    t.goto(x+(2*size), y)


def three():
    t.down()
    x = t.xcor()
    y = t.ycor()
    t.goto(x+size, y+size)
    t.goto(x, y+size)
    t.goto(x+size, y+(2*size))
    t.goto(x, y+(2*size))
    t.up()
    t.goto(x+(2*size), y)


def four():
    t.up()
    x = t.xcor()
    y = t.ycor()
    t.goto(x, y+(2*size))
    t.down()
    t.goto(x, y+size)
    t.goto(x+size, y+size)
    t.goto(x+size, y+(2*size))
    t.goto(x+size, y)
    t.up()
    t.goto(x+(2*size), y)


def five():
    t.down()
    x = t.xcor()
    y = t.ycor()
    t.goto(x+size, y)
    t.goto(x+size, y+size)
    t.goto(x, y+size)
    t.goto(x, y+(2*size))
    t.goto(x + size, y+(2*size))
    t.up()
    t.goto(x+(2*size), y)


def six():
    t.up()
    x = t.xcor()
    y = t.ycor()
    t.goto(x+size, y+(2*size))
    t.down()
    t.goto(x, y+size)
    t.goto(x, y)
    t.goto(x+size, y)
    t.goto(x+size, y+size)
    t.goto(x, y+size)
    t.up()
    t.goto(x+(2*size), y)


def seven():
    t.down()
    x = t.xcor()
    y = t.ycor()
    t.goto(x, y+size)
    t.goto(x+size, y+(2*size))
    t.goto(x, y+(2*size))
    t.up()
    t.goto(x+(2*size), y)


def eight():
    t.down()
    x = t.xcor()
    y = t.ycor()
    t.goto(x+size, y)
    t.goto(x+size, y+size)
    t.goto(x, y+size)
    t.goto(x, y+(2*size))
    t.goto(x+size, y+(2*size))
    t.goto(x+size, y+size)
    t.goto(x, y+size)
    t.goto(x, y)
    t.up()
    t.goto(x+(2*size), y)


def nine():
    t.down()
    x = t.xcor()
    y = t.ycor()
    t.goto(x+size, y+size)
    t.goto(x+size, y+(2*size))
    t.goto(x, y+(2*size))
    t.goto(x, y+size)
    t.goto(x+size, y+size)
    t.up()
    t.goto(x+(2*size), y)


defdict = {'0': zero, '1': one, '2': two, '3': three, '4': four, '5': five, '6': six, '7': seven, '8': eight, '9': nine}

negative = 0 - (len(inp) * size)    #Визначення параметрів зміщення в залежності від довжини введеного радка
t = turtle.Turtle()
t.up()
t.goto(x=negative, y=0)             # /|\ та виконання зміщення
t.pensize(5)

for i in inp:   #Запуск функцій малювальника по елементам
    bug = defdict[i]
    bug()

turtle.done()
