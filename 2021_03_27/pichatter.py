def logger(func):
    def pichatter(*args, **kwargs):
        print(f'name of function is {func.__name__}, the arguments is {args}')
    return pichatter


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(2, 3)
square_all(2, 3, 5, 6)