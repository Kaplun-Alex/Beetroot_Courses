class Person:
    def __init__(self, name, surname, age):
        self.nm = name
        self.srn = surname
        self.ag = age

    def talk(self):
        print('Ппривет меня зовут', str(self.nm), str(self.srn), 'и мне', str(self.ag), 'лет')


p = Person('Kaplun', 'Alex', 35)
p.talk()


class Dog:
    def __init__(self, agf=7):
        self.age_factor = agf

    def human_age(self):
        af = self.age_factor*7
        return af


d = Dog()
print(d.human_age())


CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self):
        self.TVCTVController = CHANNELS
        self.count_can = len(self.TVCTVController)
        self.ch_dict = {}
        for i in range(self.count_can):
            self.ch_dict[i+1] = self.TVCTVController[i]
        self.current_channel = self.ch_dict[1]

    def first_channel(self):
        return self.ch_dict[1]

    def last_channel(self):
        ls = self.TVCTVController[-1]
        return ls

    def turn_channel(self, nc):
        if nc in self.ch_dict.keys():
            tc = self.ch_dict[nc]
            self.current_channel = tc
            return tc
        else:
            print('No chanel')
            for i in self.ch_dict:
                print(str(i)+' chanel is', self.ch_dict[i])

    def next_channel(self):  #вот тут возник логический конфликт как прокручивать каналы по кругу в зависимости от количества каналов
        print(self.current_channel)
        pass

    def previous_channel(self): # Устал
        print(self.current_channel)
        pass

    def current_channel(self):
        return self.current_channel

    def is_exist(self, n):
        if n in self.ch_dict.keys():
            return 'Yes, its - ', self.ch_dict[n]
        else:
            return 'Not exist'


chan = TVController()
print(chan.ch_dict)
print('Усі канали - ', chan.TVCTVController)
print('Кількість каналів -', chan.count_can)
print('Канал що увімкнено - ', chan.current_channel)
print('Перший канал списку - ', chan.first_channel())
print('Останній канал списку - ', chan.last_channel())
print('Перемкнув на канал - ', chan.turn_channel(2))
print('Наступний канал - ', chan.next_channel())
print('Попередній канал - ', chan.previous_channel())
print(chan.is_exist(3))
