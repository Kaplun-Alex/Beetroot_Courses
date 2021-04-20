class TypeDecorators:

    def to_int(fun):
        def wrapper(*args, **kwargs):
            val = fun(*args, **kwargs)
            return int(val)

        return wrapper

    def to_bool(fun):
        def wrapper(*args, **kwargs):
            val = fun(*args, **kwargs)
            return bool(val)

        return wrapper

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

assert do_nothing('25') == 25
assert do_something('True') is True
