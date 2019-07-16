from operation.sort_data_operation.sort_data import SortOperation


def sorting(sort_choice, sort_method):
    print('\n')
    sort_data = SortOperation(sort_method)
    if sort_choice == 'salary':
        sort_data.sort_by_salary()
    elif sort_choice == 'name':
        sort_data.sort_by_name()
    else:
        print(' . . . UNDEFINIED OPERATION . . . ')
        print('. . YOU MAY INPUT WRONG CHOICE . . .')


def sort_choice_menu(sort_method):
    sort_method = str(sort_method.upper())
    notif = '\n\t{sort_method} SORT OPERATION\t\n'.format(
        sort_method=sort_method)

    print(notif)
    print('Menu : ')
    print('1. SORT SALARY DATA')
    print('2. SORT NAME DATA')
    print('\n')
    user_choice = str(input('Enter Your Choice(name/salary) -> '))
    sorting(user_choice, sort_method.lower())


def sorting_main():
    print('\tSORT DATA OPERATION\t\n')
    print('Menu : ')
    print('1. ASCENDING SORTING( enter asc )')
    print('2. DESCENDING SORTING( enter desc )\n')
    user_choice = str(input('Enter Your Choice(asc/desc) -> '))
    sort_method = str(user_choice.upper())
    sort_choice_menu(sort_method)
