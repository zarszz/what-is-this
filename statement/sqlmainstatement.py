def getNameStatement(searchedName):

    sql_search_statement = "SELECT id FROM company " \
                           "WHERE name='{searchedName}';"
    sql_statement = sql_search_statement.format(searchedName=searchedName)

    return sql_statement


def get_address_statement(choice, userId):

    update_data = str(input('Enter New Employee Address : '))
    sql_statement = "UPDATE company SET address='{update_data}' " \
                    "WHERE id={userId};"
    sql_query = sql_statement.format(
        update_data=update_data, userId=userId)

    return sql_query


def get_name_statement(choice, userId):

    update_data = str(input('Enter New Employee Name : '))
    sql_statement = "UPDATE company SET name='{update_data}' " \
                    "WHERE id={userId};"
    sql_query = sql_statement.format(
        update_data=update_data, userId=userId)

    return sql_query


def get_age_statement(choice, userId):
    update_data = int(input('Enter New Employee Age: '))
    sql_statement = "UPDATE company SET age='{update_data}' WHERE id={userId};"
    sql_query = sql_statement.format(
        update_data=update_data, userId=userId)

    return sql_query


def get_salary_statement(choice, userId):
    update_data = float(input('Enter New Employee Salary : '))
    sql_statement = "UPDATE company SET salary='{update_data}' " \
                    "WHERE id={userId};"
    sql_query = sql_statement.format(
        update_data=update_data, userId=userId)

    return sql_query


def get_sort_salary_statement(sort_method):
    sort_operation = sort_method.upper()
    sql_statement = "SELECT name, salary FROM company " \
                    "ORDER BY salary {sort_operation};"
    sql_query = sql_statement.format(sort_operation=sort_operation)
    return sql_query


def get_sort_name_statement(sort_method):
    sort_operation = sort_method.upper()
    sql_statement = "SELECT name FROM company " \
                    "ORDER BY name {sort_operation};"
    sql_query = sql_statement.format(sort_operation=sort_operation)
    return sql_query


def get_max_salary_statement():
    sql_statement = "SELECT name,salary FROM company "\
                    "WHERE salary = (SELECT MAX (salary) FROM company);"
    return sql_statement


def get_min_salary_statement():
    sql_statement = "SELECT name,salary FROM company "\
                    "WHERE salary = (SELECT MIN (SALARY) FROM company);"
    return sql_statement


def get_average_salary_statement():
    sql_statement = "SELECT AVG(salary) FROM company;"
    return sql_statement
