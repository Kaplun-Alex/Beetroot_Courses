def arg_rules(type_: type, max_length: int, contains: list):    #нэ ну тут понятно все, херак и все работает!
    def actual_dec(f):
        def wrapper(*args, **kwargs):
            print(args[0])
            if type(args[0]) == type_:
                pass
            else:
                print('Not string')
                return False
            if len(args[0]) < max_length:
                pass
            else:
                print(f'The args is more len when set rules')
                return False
            for i in contains:
                fnd = args[0].find(i)
                if fnd == -1:
                    print('Some symbols not find')
                    return False
                else:
                    pass

            rez = f(*args, **kwargs)
            print(rez)
            return rez
        return wrapper
    return actual_dec


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
