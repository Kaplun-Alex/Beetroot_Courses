import functools as fc


def decorator(f):
    @fc.wraps(f)
    def wrapper_decor(*args, **kwargs):
        val = f(*args, **kwargs)
        return val
    return wrapper_decor

@decorator
def creator(crt):
    return f'{crt}'

print(creator('dich'), creator.__name__)