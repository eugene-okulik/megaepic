from random import randrange, random


def check_bonus_for_give_salary():
    salary = int(input('Сколько salary? '))
    bonus = bool(randrange(2))
    if bonus:
        salary += random()
    print(salary, bonus)

    
check_bonus_for_give_salary()
