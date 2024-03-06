PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


new_list = PRICE_LIST.split()
new_array = list(map(lambda x: x.replace('р', ''), new_list))
new_dict = dict(zip(new_list[::2], map(int, new_array[1::2])))
print(new_dict)
