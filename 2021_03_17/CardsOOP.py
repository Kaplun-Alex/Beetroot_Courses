import random


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} - {self.suit}'


class Koloda:
    def __init__(self):
        self.cards = []
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'D', 'K', 'T']
        suits = ['♤', '♧', '♡', '♢']
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def giv_me_one(self):
        card = self.cards.pop()
        remainder = len(self.cards)
        print(card, 'Осталось - ', remainder)

    def open_deck(self):
        for card in self.cards:
            print(card)


class Box:
    def __init__(self):
        self.box = []

    def __repr__(self):
        return f'{self.box}'

    def prnt(self):
        print(self.box)

    def add_in_box(self, card):
        self.box.append(card)
        pass


class Stol:
    def __init__(self): # создали 12 ячеек которые есть в пасьянсе на столе
        self.list_of_box = []
        for i in range(12):
            self.list_of_box.append(Box())
            print(self.list_of_box)

    def insert_cards_on_main_box(self, koloda):
        for i in koloda:
            print(i)
            self.list_of_box[0].add_in_box(i)
        print(koloda)
        pass



    def see_Stol(self):
        print(self.list_of_box)
        print(len(self.list_of_box))


def main():
    d = Koloda()
    d.open_deck()
    print('***************')
    d.shuffle()
    d.open_deck()
    print('***************')
    d.giv_me_one()
    d.giv_me_one()
    d.giv_me_one()
    st = Stol()
#    st.see_Stol()
    b = Box()
    b.prnt()
    pass


if __name__ == '__main__':
    main()
