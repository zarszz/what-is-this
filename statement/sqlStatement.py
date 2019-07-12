from statement.sqlmainstatement import *

def getSqlStatement(choice, userId):
    if(choice == 'address'):
        sql_statement = get_address_statement(choice, userId)
        return sql_statement
    if(choice == 'age'):
        sql_statement = get_age_statement(choice, userId)
        return sql_statement
    if(choice == 'name'):
        sql_statement = get_name_statement(choice, userId)
        return sql_statement
    if(choice == 'salary'):
        sql_statement = get_salary_statement(choice, userId)
        return sql_statement
