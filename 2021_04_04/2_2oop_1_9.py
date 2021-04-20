class Phonefil:
    def __init__(self, ls):
        self.ls = ['+380' + ls[j].replace(' ', '') for j in range(len(ls)) if ls[j].find('097') == 0 or ls[j].find('050') == 0]
        self.counter = 0
    def __iter__(self):
        self.counter = self.counter
        return self
    def __next__(self):
        n = self.counter
        if n != len(self.ls):
            self.counter += 1
            return self.ls[n]
        else:
            raise StopIteration


phones = ['044 225 73 39', '099 116 30 87', '094 129 81 69', '094 127 04 85', '044 222 74 33', '044 353 55 31',
          '097 921 27 09', '094 550 50 02', '044 362 96 00', '097 853 55 81', '097 120 95 90', '099 752 22 97',
          '050 761 49 45', '094 497 75 09', '094 498 89 53', '094 496 13 91', '094 497 35 13', '094 497 75 69',
          '050 063 52 97', '050 530 97 71', '044 227 16 63', '056 785 55 19', '068 450 69 13', '097 001 42 67',
          '096 097 58 16', '094 497 34 37', '094 097 12 17', '094 497 75 69', '097 497 75 97', '094 497 34 85',
          '094 496 52 54']
t = Phonefil(phones)
for i in t:
    print(i)