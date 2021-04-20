class GreatNumerator:
    def __init__(self, ls):
        self.ls = [str(j) + " " + ls[j] for j in range(len(ls))]
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
lists = ['111', 'cat', 'got', 'ddd', '222']
t = GreatNumerator(lists)
for i in t:
    print(i)
