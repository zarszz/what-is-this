from statement.sqlmainstatement import *

def getSqlStatement(choice, userId=None, sort_method=None, employee_name=None):
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
    if choice == 'get_row_number':
        sql_statement = get_all_data()
    if choice == 'get_one_employee_name':
        sql_statement = get_one_name_statement(employee_name)
    if choice == 'get_data_by_name':
        sql_statement = get_data_by_name(employee_name)
    if choice == 'get_id_from_name':
        sql_statement = get_id_from_name(employee_name)
    return sql_statement
