class Flowers:
    root = True

    def __init__(self, name, price, color, life_time, stem):
        self.name = name
        self.price = price
        self.color = color
        self.life_time = life_time
        self.stem = stem


class Rose(Flowers):
    def __init__(self, price, color, life_time, stem):
        super().__init__('Роза', price, color, life_time, stem)


class Tulpane(Flowers):
    def __init__(self, price, color, life_time, stem):
        super().__init__('Тюльпан', price, color, life_time, stem)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calc(self):
        price = 0
        for flower in self.flowers:
            price += flower.price
        return price

    def die_time(self):
        time = 0
        for flower in self.flowers:
            time += flower.life_time
        avg_life = time / len(self.flowers)
        return avg_life

    def find_flower_avg_life_time(self, life_time):
        favorite_flower = [flower for flower in self.flowers if flower.life_time == life_time]
        return favorite_flower

    def sort_flowers_by_stem(self):
        self.flowers.sort(key = lambda x:x.stem, reverse = True)

    def sort_flowers_by_price(self):
        self.flowers.sort(key = lambda x:x.price, reverse = True)

    def sort_flower_by_color(self):
        self.flowers.sort(key = lambda x:x.color)


red_rose = Rose(55, 'Red', 32, 112)
yellow_tulpane = Tulpane(77, 'Yellow', 66, 114)

bouquet = Bouquet()
bouquet.add_flower(red_rose)
bouquet.add_flower(yellow_tulpane)


favorite_flower = bouquet.find_flower_avg_life_time(5)
for flower in favorite_flower:
    print(flower.name)


total_price = bouquet.calc()
print(f"Стоимость равна: {total_price} ")


total_life_time = bouquet.die_time()
print(f"Время жизни: {total_life_time}")


bouquet.sort_flowers_by_stem()
bouquet.sort_flower_by_color()
bouquet.sort_flowers_by_price()
