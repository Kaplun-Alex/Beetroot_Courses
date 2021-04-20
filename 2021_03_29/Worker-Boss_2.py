class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def __str__(self):
        return f'Мой бос {self.name}'

    def get_workers_list(self):
        return self._workers

    def set_workers(self, worker):
        self._workers.append(worker)

    def del_w(self, indx):
        del self._workers[indx]

    workers = property(get_workers_list, set_workers, del_w) # непойму почему тут отсвечивает Deleter signature should be (self) ?


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    def __repr__(self):
        return self.name

    def get_boss(self):
        return self._boss

    def set_new_bos(self, b):
        if isinstance(b, Boss):
            self._boss = b
        else:
            print('Он не бос, а канцелярская крыса')

    boss = property(get_boss, set_new_bos)
oleksa = Boss(1, 'Пекельний Олекса', 'Сеньйор Памидор')
fat_oleksa = Boss(1, 'Товстий Олекса', 'Сеньйор Памидор')
kaziavka = Worker(0, 'Казявка', 'Сеньйор Памидор', oleksa)
pukavka = Worker(0, 'Пукавка', 'Сеньйор Памидор', oleksa)
oleksa.workers = kaziavka
oleksa.workers = pukavka
print(oleksa._workers)
del oleksa.workers[0]
print(oleksa._workers)
kaziavka.boss = fat_oleksa
print(kaziavka.boss)
