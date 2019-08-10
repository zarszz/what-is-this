from statement.sqlmainstatement import (
            get_address_statement, get_age_statement,
            get_name_statement, get_salary_statement,
            get_max_salary_statement, get_min_salary_statement,
            get_sort_name_statement, get_sort_salary_statement)


def getSqlStatement(choice, userId=None, sort_method=None):
    if choice == 'address':
        sql_statement = get_address_statement(choice, userId)
    if choice == 'age':
        sql_statement = get_age_statement(choice, userId)
    if choice == 'name':
        sql_statement = get_name_statement(choice, userId)
    if choice == 'salary':
        sql_statement = get_salary_statement(choice, userId)
    if choice == 'max':
        sql_statement = get_max_salary_statement()
    if choice == 'min':
        sql_statement = get_min_salary_statement()
    if choice == 'get_sort_name':
        sql_statement = get_sort_name_statement(sort_method)
    if choice == 'get_sort_salary':
        sql_statement = get_sort_salary_statement(sort_method)
    return sql_statement
