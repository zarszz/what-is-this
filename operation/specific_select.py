from operation.connector import conn as connector

def get_name():
    '''
    '''
    employee_name = str(input('Enter Employee Name : '))

    from operation.validation.userValidation import employeeNameValidation
    validation = employeeNameValidation(employee_name, True)
    
    if (validation is True):
        return employee_name
    elif (validation is False):
        return None

def select_specific_by_data(choice):
    '''
    '''
    sql_connection = connector()
    employee_name = get_name()
    if employee_name is not None:
        db_cursor = sql_connection.cursor()
        sql_statement = "SELECT name, {choice} FROM company WHERE name='{employee_name}'"
        sql_query = sql_statement.format(choice=choice, employee_name=employee_name)
        db_cursor.execute(sql_query)
        results = db_cursor.fetchone()
        print('Name    = ', str(results[0]).capitalize())
        string_result = '{choice} = ' +  results[1]
        string_results = string_result.format(choice=str(choice).capitalize())
        print(string_results)
