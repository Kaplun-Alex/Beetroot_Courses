def get_me():
    def go_away(g):
        if g == 0:
            print('Go avay dude')
        elif g == 1:
            print('Come to me')
        else:
            print('LoL')
    return go_away

x = get_me()
x(1)
x(0)
x(10)
