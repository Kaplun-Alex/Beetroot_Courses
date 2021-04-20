import functools as fc


def do_twice(f):
    @fc.wraps(f)
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        return f(*args, **kwargs)
    return wrapper

