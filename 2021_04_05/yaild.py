def GreatNumerator(lists):
    work_list = [str(j) + ' ' + lists[j] for j in range(len(lists))]
    for x in work_list:
        yield x

strings = ['111', 'cat', 'got', 'ddd', '222']
for i in GreatNumerator(strings):
    print(i)


phones = ['044 225 73 39', '099 116 30 87', '094 129 81 69', '094 127 04 85', '044 222 74 33', '044 353 55 31',
          '097 921 27 09', '094 550 50 02', '044 362 96 00', '097 853 55 81', '097 120 95 90', '099 752 22 97',
          '050 761 49 45', '094 497 75 09', '094 498 89 53', '094 496 13 91', '094 497 35 13', '094 497 75 69',
          '050 063 52 97', '050 530 97 71', '044 227 16 63', '056 785 55 19', '068 450 69 13', '097 001 42 67',
          '096 097 58 16', '094 497 34 37', '094 097 12 17', '094 497 75 69', '097 497 75 97', '094 497 34 85']


def Phonefil(phones, operation: int):
    if operation == 1:
        work_list = [x for x in phones if x[:3] == '097']
        for j in work_list:
            yield j
    elif operation == 2:
        work_list = [x for x in phones if x[:3] == '097' or x[:3] == '050']
        for j in work_list:
            yield j
    elif operation == 3:
        work_list = ['+38' + x.replace(' ', '') for x in phones if x[:3] == '097' or x[:3] == '097']
        for j in work_list:
            yield j
    else:
        raise StopIteration


for i in Phonefil(phones, 1):
    print(i)
for i in Phonefil(phones, 2):  #как не странно повторно работает без заморочек
    print(i)
for i in Phonefil(phones, 3):
    print(i)
for i in Phonefil(phones, 0):
    print(i)
