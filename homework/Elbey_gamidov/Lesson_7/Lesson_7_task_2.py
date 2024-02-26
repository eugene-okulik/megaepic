words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def how_much_times(dict):
    for key, value in words.items():
        for i in range(value):
            print(key, end='')
        print()

how_much_times(words)
