import os

from operation.sort_data_operation.sort_data import SortOperation


def sorting(sort_choice, sort_method):
    print('\n')
    os.system("clear")
    print("\t" + sort_method.upper() + " SORTING" + "\t\n")
    print("Data Will Sorted : " + sort_choice.title() + "\n")
    sort_data = SortOperation(sort_method, sort_choice)
    print(sort_data.sort_method)
    sort_data.run_sort_data()
    if sort_choice not in('salary', 'name'):
        print(' . . . UNDEFINIED OPERATION . . . ')
        print('. . YOU MAY INPUT WRONG CHOICE . . .')


def sort_choice_menu(sort_method):
    os.system('clear')
    sort_method = str(sort_method.upper())
    notif = '\n\t{sort_method} SORT OPERATION\t\n'.format(
        sort_method=sort_method)

    print(notif)
    print('Menu : ')
    print('1. SORT SALARY DATA')
    print('2. SORT NAME DATA')
    print('\n')
    user_choice = str(input('Enter Your Choice -> '))
    if user_choice == "1":
        user_choice = "salary"
    elif user_choice == "2":
        user_choice = "name"
    sorting(user_choice, sort_method.lower())


def sorting_main():
    os.system('clear')
    print('\tSORT DATA OPERATION\t\n')
    print('Menu : ')
    print('1. ASCENDING SORTING ')
    print('2. DESCENDING SORTING\n')
    user_choice = str(input('Enter Your Choice -> '))
    if user_choice == "1":
        user_choice = "asc"
    elif user_choice == "2":
        user_choice = "desc"
    sort_method = str(user_choice.upper())
    sort_choice_menu(sort_method)
