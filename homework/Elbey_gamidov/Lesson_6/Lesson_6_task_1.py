text = '''Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'''  # Правильно перенес строку? а то линт ругается

words = text.split()
fin_words = []
for word in words:
    if word.endswith(','):
        new_word = word.replace(',', '')
        fin_words.append('ing' + str(new_word) + str(','))
    elif word.endswith('.'):
        second_new_word = word.replace('.', '')
        fin_words.append('ing' + str(second_new_word) + str('.'))
    else:
        fin_words.append('ing' + str(word))
print(' '.join(fin_words))
