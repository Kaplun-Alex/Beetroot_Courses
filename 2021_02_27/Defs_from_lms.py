def favorite_movie():
    inp =input('Hi dude, what is your favorite movie: ')
    print('Your favorite movie is ', inp)


# faoirite_movie()

#////////////////////////////////////////////////////////
c = {}


def make_country():
    name = input('Input country: ')
    capital = input('Input dsgsdfgcapital: ')
    c[name] = capital


def print_country(x):
    print(x)


#make_country()


#print_country(c)


#//////////////////////////////////////////////


def calc(op, args):
    print(op)
    print(args)
    if op == '-':
        res = int(args[0])
        for i in args[1:]:
            res = res - int(i)
            print(res)
    elif op == '+':
        res = 0
        for i in args:
            res = res + int(i)
            print(res)
    elif op == '*':
        res = 1
        for i in args:
            res = res * int(i)
            print(res)
    else:
        print('Kosyak')


def inp_calc():
    op = input('Add operator dude: ')
    args = []
    args.append(input('Add int: '))
    args.append(input('Add int: '))
    trh = '1'
    while trh == '1':
        trh = (input('More - 1/Enough - 0: '))
        if trh == '1':
            args.append(input('Add int: '))
        else:
            print('input done')
    print(args)
    calc(op, args)



#inp_calc()


#/////////////////////////////////////////////////////
