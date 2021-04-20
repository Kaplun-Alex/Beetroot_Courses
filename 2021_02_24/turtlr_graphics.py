import turtle

inp = []
for i in (input('Введи 10 цифр братюня: ')):
    inp.append(i)
print(inp)
negative = 0-(len(inp)*50)
t = turtle.Turtle()
t.up()
t.goto(x=negative, y=0)
t.pensize(5)


def zero():
    t.down()
    x = t.xcor()
    y = t.ycor()
    t.goto(x+50, y)
    t.goto(x+50, y+100)
    t.goto(x, y+100)
    t.goto(x, y)
    t.up()
    t.goto(x+100, y)


def one():
    t.up()
    x = t.xcor()
    y = t.ycor()
    t.goto(x, y+50)
    t.down()
    t.goto(x+50, y+100)
    t.goto(x+50, y)
    t.up()
    t.goto(x+100, y)


def two():
    t.up()
    x = t.xcor()
    y = t.ycor()
    t.goto(x, y+100)
    t.down()
    t.goto(x+50, y+100)
    t.goto(x+50, y+50)
    t.goto(x, y)
    t.goto(x+50, y)
    t.up()
    t.goto(x+100, y)


def three():
    t.down()
    x = t.xcor()
    y = t.ycor()
    t.goto(x+50, y+50)
    t.goto(x, y+50)
    t.goto(x+50, y+100)
    t.goto(x, y+100)
    t.up()
    t.goto(x+100, y)


def four():
    t.up()
    x = t.xcor()
    y = t.ycor()
    t.goto(x, y+100)
    t.down()
    t.goto(x, y+50)
    t.goto(x+50, y+50)
    t.goto(x+50, y+100)
    t.goto(x+50, y)
    t.up()
    t.goto(x+100, y)


def five():
    t.down()
    x = t.xcor()
    y = t.ycor()
    t.goto(x+50, y)
    t.goto(x+50, y+50)
    t.goto(x, y+50)
    t.goto(x, y+100)
    t.goto(x + 50, y+100)
    t.up()
    t.goto(x+100, y)


def six():
    t.up()
    x = t.xcor()
    y = t.ycor()
    t.goto(x+50, y+100)
    t.down()
    t.goto(x, y+50)
    t.goto(x, y)
    t.goto(x+50, y)
    t.goto(x+50, y+50)
    t.goto(x, y+50)
    t.up()
    t.goto(x+100, y)


def seven():
    t.down()
    x = t.xcor()
    y = t.ycor()
    t.goto(x, y+50)
    t.goto(x+50, y+100)
    t.goto(x, y+100)
    t.up()
    t.goto(x+100, y)


def eight():
    t.down()
    x = t.xcor()
    y = t.ycor()
    t.goto(x+50, y)
    t.goto(x+50, y+50)
    t.goto(x, y+50)
    t.goto(x, y+100)
    t.goto(x+50, y+100)
    t.goto(x+50, y+50)
    t.goto(x, y+50)
    t.goto(x, y)
    t.up()
    t.goto(x+100, y)


def nine():
    t.down()
    x = t.xcor()
    y = t.ycor()
    t.goto(x+50, y+50)
    t.goto(x+50, y+100)
    t.goto(x, y+100)
    t.goto(x, y+50)
    t.goto(x+50, y+50)
    t.up()
    t.goto(x+100, y)


defdict = {'0': zero, '1': one, '2': two, '3': three, '4': four, '5': five, '6': six, '7': seven, '8': eight, '9': nine}

for i in inp:
    bug = defdict[i]
    bug()

turtle.done()
