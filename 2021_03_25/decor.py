from datetime import datetime
from decorators import do_twice

def my_decorator(f):
    def wrapper():
        print('Something is happening before')
        f()
        print('Something is happening after')
    return wrapper()

def say_wh():
    print('Whh!')

# say_wh = my_decorator(say_wh)
#/////////////////////////////////////////////////

def not_during_the_night(f):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            f()
        else:
            pass
    return wrapper

def say_ya_aru():
    print('YA ARU!')

say_ya_aru = not_during_the_night(say_ya_aru)
say_ya_aru()

#//////////////////////////////////////////////

def my_decor(f):
    def wrapper():
        print('Something is happening before')
        f()
        print('Something is happening after')

    return wrapper

@my_decor
def say_wh2():
    print('Whh!')
say_wh2()

#////////////////////////////////////////////////

@do_twice
def say_dohera():
    print('dohera')
say_dohera()

#///////////////////////////////////////////////

@do_twice
def greet(name):
    print(f'Прувэт братуха {name}')
greet('World')

#///////////////////////////////////////////////

@do_twice
def return_grt(name):
    print('Crt grt')
    return f'Hi {name}'

hi_chucha = return_grt('Chucha')
print(hi_chucha)