from operation.connector import conn
from statement.sqlmainstatement import(
    get_sort_name_statement, get_sort_salary_statement
)


class SortOperation():
    '''
    '   Sorting selecting row in database
    '   params :
    '   1). default is None or operation not permitted
    '   2). desc is sorting selected data by name by descending
    '   3). asc  is sorting selected data by name by ascending
    '''

    def __init__(self, sort_method):
        self.sort_method = sort_method

    def sort_by_salary(self):
        db_connector = conn()

        check_method = self.sort_method
        sql_statement = get_sort_salary_statement(check_method)

        db_cursor = db_connector.cursor()
        db_cursor.execute(sql_statement)
        sort_row_data = db_cursor.fetchone()

        i = 1
        while sort_row_data is not None:
            print(i, '-> Name   = ', sort_row_data[0])
            print('     Salary = ', sort_row_data[1], '\n')
            sort_row_data = db_cursor.fetchone()
            i = i + 1

    def sort_by_name(self):
        db_connector = conn()

        check_method = self.sort_method
        sql_statement = get_sort_name_statement(check_method)

        db_cursor = db_connector.cursor()
        db_cursor.execute(sql_statement)
        sort_row_data = db_cursor.fetchone()

        i = 1
        while sort_row_data is not None:
            print(i, '-> Name   = ', sort_row_data[0], '\n')
            sort_row_data = db_cursor.fetchone()
            i = i + 1