from os import system

from get_max import get_max_salary
from beauti.sql_menu_beauti import beauti_menu


def sql_menu():
    system('clear')
    print(beauti_menu())
    print('\n')
    print('1. Get Max Salary')
    print('2. Get Min Salary')

    choice = str(input('Your choice -> '))

    if choice == '1':
        get_max_salary()
    if choice == '2':
        pass
