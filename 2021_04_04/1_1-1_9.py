# 1.1////////////////////////////////////////////////////////
def generator(n):
    print('1.1////////////////////////')
    return (str(x) for x in range(n))
for x in generator(10):
    print(x)

# 1.2 /////////////////////////////////////////////////////////
l = ['кит', 'кот', 'крот']
def en_generator(n):
    return [str(j) + ' ' + n[j] for j in range(len(n))]
z = en_generator(l)
print(z)
def en_generator_obj(n):
    print('1.2 ////////////////////////')
    return (str(j) + ' ' + n[j] for j in range(len(n)))
for x in en_generator_obj(l):
    print(x)

# 1.3 /////////////////////////////////////////////////
def en_generator_obj(n):
    print('1.3///////////////////')
    return (str(j) + ' ' + n[j] for j in range(len(n)) if len(n[j]) <= 3)
for x in en_generator_obj(l):
    print(x)

# 1.4 /////////////////////////////////////////////////
lists0 = ['111', 'cat', 'got', 'ddd', '222']
def en_generator_obj_digit(n):
    print('1.4///////////////////')
    return (n[j] for j in range(len(n)) if n[j].isdigit())
for x in en_generator_obj_digit(lists0):
    print(x)

# 1.5///////////////////////////////////////////////////
def en_generator_obj_strnum(n):
    print('1.5///////////////////')
    return (j for j in range(len(n)) if n[j].isdigit())
for x in en_generator_obj_strnum(lists0):
    print(x)

# 1.6///////////////////////////////////////////////////
def en_generator_obj_cort(n):
    print('1.6///////////////////')
    return ((j, n[j]) for j in range(len(n)) if n[j].isdigit())
for x in en_generator_obj_cort(lists0):
    print(x)

# 1.7///////////////////////////////////////////////////
phones = ['044 225 73 39', '099 116 30 87', '094 129 81 69', '094 127 04 85',
          '044 222 74 33', '044 353 55 31', '097 921 27 09', '094 550 50 02',
          '044 362 96 00', '097 853 55 81', '097 120 95 90', '099 752 22 97',
          '050 761 49 45', '094 497 75 09', '094 498 89 53', '094 496 13 91',
          '094 497 35 13', '094 497 75 69', '050 063 52 97', '050 530 97 71',
          '044 227 16 63', '056 785 55 19', '068 450 69 13', '097 001 42 67',
          '096 097 58 16', '094 497 34 37', '094 097 12 17', '094 497 75 69',
          '097 497 75 97', '094 497 34 85', '094 496 52 54']

def en_generator_obj_phone(n):
    print('1.7///////////////////')
    return (n[j] for j in range(len(n)) if n[j].find('097') == 0)
for x in en_generator_obj_phone(phones):
    print(x)

# 1.8///////////////////////////////////////////////////
def en_generator_obj_phone1(n):
    print('1.8///////////////////')
    return (n[j] for j in range(len(n)) if n[j].find('097') == 0 or n[j].find('050') == 0)
for x in en_generator_obj_phone1(phones):
    print(x)

# 1.9 /////////////////////////////////////////////////////////
def en_generator_obj_plus(n):
    print('1.9///////////////////')
    return ('+380' + n[j].replace(' ', '') for j in range(len(n)) if n[j].find('097') == 0 or n[j].find('050') == 0)
for x in en_generator_obj_plus(phones):
    print(x)