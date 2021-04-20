class Animal:
    def __init__(self, an):
        self.animal = an

    def __str__(self):
        return self.animal

    def talk(self, say='Сыш? сюда иди!'):
        return self.animal + say


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, an)
        self.dog = 'Dog'

    def __str__(self):
        return f'{self.animal} {self.dog} say - The gay! the gay!'


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self, an)
        self.Cat = 'Cat'

    def __str__(self):
        return f'{self.animal} {self.Cat} say - The meoW, the meoW!'


an = Animal('Зверюга')
dg = Dog()
ct = Cat()
print(an)
print(dg)
print(ct)
