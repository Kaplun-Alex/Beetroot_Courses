import random

rn = random.Random()


def vperer(t, n):
    anger = rn.randint(0, 360)
    t.forward(n)
    t.right(anger)


def vperedl(t, n):
    anger = rn.randint(0, 360)
    t.forward(n)
    t.left(anger)


