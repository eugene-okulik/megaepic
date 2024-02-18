my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1, 2, 3, 4, 5],
    'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
    'set': {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
}


print(my_dict['tuple'][-1])
my_dict['list'].append(12)
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = ('first', )
my_dict['dict'].pop('one')
my_dict['set'].add(10)
my_dict['set'].remove('Monday')
print(my_dict)
