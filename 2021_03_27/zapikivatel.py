def stop_words(words: list):    # сюда попал список стоп слов, только для того чтобы он прошел ниже
    def actual_dec(f):  # сюда попала функция create_slogan
        def wrapper(*args, **kwargs):    # сюда попали аргументы reate_slogan
            rez = f(*args, **kwargs)   # выполняем create_slogan для того чтобы получить стив глушит водичку в rez
            print(type(rez), rez)   # проверяем что переменная в адеквате и стринг
            for i in words:     # Перебираем аргументы дескриптора
                print(i)    # проверяем что аргументы прилетели правильно а не сразу списком в кортеже и все это словарем во множемтве
                rez = rez.replace(i, '*') # заменяем
            print(rez)
            return rez
        return wrapper
    return actual_dec


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


