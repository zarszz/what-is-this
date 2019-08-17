from operation.connector import conn as connector
from operation.validation.userValidation import(
        employeeNameValidation as employee_name_validation)
from statement.sqlmainstatement import get_specific_select

def get_name():
    '''
    '''
    employee_name = str(input('Enter Employee Name : '))

    validation = employee_name_validation(employee_name, True)

    if validation is True:
        return employee_name


def select_specific_by_data(choice):
    '''
    '''
    sql_connection = connector()
    employee_name = get_name()
    if employee_name is not None:
        
        db_cursor = sql_connection.cursor()
        db_cursor.execute(get_specific_select(choice, employee_name))

        results = db_cursor.fetchone()
        print(results)
        print('Name \t= ', str(results[0]).capitalize())
        string_result = '{choice} = ' + str(results[1])
        string_results = string_result.format(choice=str(choice))
        print(string_results)
        db_cursor.close()
    sql_connection.close()
