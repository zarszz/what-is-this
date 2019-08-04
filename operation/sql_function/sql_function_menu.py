from os import system
from operation.sql_function.get_max import get_max_salary
from operation.sql_function.get_min import get_min_salary
from operation.sql_function.get_aveg_salary import get_average_salary
from beauti.sql_menu_beauti import beauti_menu


def sql_menu():
    system('clear')
    print(beauti_menu())
    print('\n')
    print('1. Get Max Salary')
    print('2. Get Min Salary')
    print('3. Get Average Salary')

    choice = str(input('Your choice -> '))

    if choice == '1':
        get_max_salary()
    if choice == '2':
        get_min_salary()
    if choice == '3':
        get_average_salary()
