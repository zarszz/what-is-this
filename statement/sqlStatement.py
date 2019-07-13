from statement.sqlmainstatement import (
            get_address_statement, get_age_statement,
            get_name_statement, get_salary_statement
            )


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
