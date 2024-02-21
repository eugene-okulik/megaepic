text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

words = text.split() # Перевел все в массив  
fin_words = []  # Завел новый массив
for word in words:  # Иду по циклу
    if word.endswith(','):  # Если слово заканчивается на запятую
        new_word = word.replace(',', '')  # то меняю запятую на ничто
        fin_words.append(new_word)  # пушу слово в новый массив
    elif word.endswith('.'):  # Тут тоже самое, но с точкой
        second_new_word = word.replace('.', '')
        fin_words.append(second_new_word)        
    else:
        fin_words.append(word)
print('ing '.join(fin_words))  # добавляю ing к каждому слову