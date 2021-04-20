def secondex():
    import turtle
    tur = turtle.Turtle()
    f = open('move.txt', 'r', encoding='utf8')
    t = f.read()
    f.close()
    t = t.split('\n')
    doublet = []
    for i in t:
        s = i.split(', ')
        doublet.append(s)
    for i in doublet:
        tur.dot(10)
        tur.pensize(4)
        x = int(i[0])
        y = int(i[1])
        color = i[2]
        tur.color(color)
        tur.goto(x, y)

    turtle.done()


def secondplus():
    import turtle
    import random
    rn = random.Random()
    tur = turtle.Turtle()
    tur.pensize(4)
    for i in range(0, 20):
        x = rn.randint(-300, 300)
        y = rn.randint(-300, 300)
        tur.color('green')
        tur.goto(x, y)
    x = 0
    while x != 20:
        anger = rn.randint(0, 360)
        tur.left(anger)
        line = rn.randint(-50, 500)
        tur.forward(line)
        x += 1

    turtle.done()


#secondex()
#secondplus()
