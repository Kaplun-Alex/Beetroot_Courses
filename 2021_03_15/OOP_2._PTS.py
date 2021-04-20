class Person:
    def __init__(self, name, surname, pobatiuschka, age, sex, nationality):
        self.name = name
        self.surname = surname
        self.pbts = pobatiuschka
        self.age = age
        self.sex = sex
        self.nationalyty = nationality

    def person_info(self):
        print(self.name, self.surname, self.pbts, self.age, self.sex, self.nationalyty)


class Student(Person):
    def __init__(self, fak, gruppa, name, surname, pobatiuschka, age, sex, nationality):
        super().__init__(name, surname, pobatiuschka, age, sex, nationality)
        self.fak = fak
        self.gruppa = gruppa

    def student_info(self):
        print(self.fak, self.gruppa, self.name, self.surname, self.pbts, self.age, self.sex, self.nationalyty)


class Teacher(Person):
    def __init__(self, predmet, relation, name, surname, pobatiuschka, age, sex, nationality):
        super().__init__(name, surname, pobatiuschka, age, sex, nationality)
        self.predmet = predmet
        self.relation = relation

    def teacher_info(self):
        print(self.predmet, self.relation, self.name, self.surname, self.pbts, self.age, self.sex, self.nationalyty)


t1 = Teacher('Мафматика', 'Злий як собака', 'Уасілій', 'Уасільській', 'Уасілієвіч', 'Олдос', 'Мужлан', 'Хохол')
print(t1)
t1.teacher_info()

p1 = Student('Массового розпіздяйства', '1-Ж', 'Ваня', 'Ванський', 'Уасілієвіч', 'Шмаркач', 'Пацан', 'Хохолок')
print(p1)
p1.student_info()

t1.person_info()
p1.person_info()


class Mathematician:
    def square_nums(self, ssquad):
        print(ssquad)
        rez = []
        for i in ssquad:
            rez.append(i ** 2)
        print(rez)
        return rez

    def remove_positives(self, sswnegative):
        print(sswnegative)
        rez = list(filter(lambda x: x < 0, sswnegative))    # я і забув, але нагуглив
        print(rez)
        return rez

    def filter_leaps(self, ssyear):
        print(ssyear)
        rez = list(filter(lambda x: x % 4 == 0, ssyear))    #
        print(rez)
        return rez
'''
Чомусь ругаэться що методи повинні бути статичними, але працює. Проти індусна якась Хєрь.
'''

m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
