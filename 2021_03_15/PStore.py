class Product:
    def __init__(self, tupe: str, name: str, price: int):  #type - шадовс еррор
        if type(tupe) == str:
            self.type = tupe
        else:
            print('Error...')

        if type(name) == str:
            self.name = name
        else:
            print('Error...')

        if type(price) == int:
            self.price = price
        else:
            print('Error...')


class ProductStore:
    def __init__(self):
        self.magaz = {}
        self.kapusta = 0

    def add(self, product, amount):
        if product not in self.magaz.keys():
            product.price *= 1.3
            self.magaz[product] = amount
            print('Новий продукт додано!')
        else:
            print('Кількість продукту додано')
            self.magaz[product] += amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        pass

    def sell_product(self, product_name, amount):
        if self.magaz[product_name] > amount:   # Проверка на количество продуктов в магазе
            if product_name in self.magaz.keys():
                self.magaz[product_name] -= amount
                print('продано, осталось - ', self.magaz[product_name])
                self.kapusta = amount*product_name.price
            else:
                print('Немає продукту в магазі')
        else:
            print('Продукту немає або його не вистачає')

    def get_income(self):
        print(self.kapusta)

    def get_all_products(self):
        for i in self.magaz:
            print(i.name, i.price, i.type)

    def product_info(self, product_name):
        pass


p = Product('Sport', 'Football T-Shirt', 100)
print('Price as product p1', p.price)
p2 = Product('Food', 'Ramen', 100)
print('Price as product p2', p2.price)
s = ProductStore()

s.add(p, 10)
print('Price as product p1 in magaz', p.price)
s.add(p2, 300)
print('Price as product  p1 in magaz', p.price)
s.sell_product(p, 5)

print(s.get_all_products())
