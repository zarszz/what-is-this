from operation.connector import conn
from statement.sqlmainstatement import(
    get_sort_name_statement, get_sort_salary_statement)
from statement.sqlStatement import(
        getSqlStatement as get_sql_statement)

class SortOperation():
    '''
        sort_method in params is for get sorting method, example
        sort_operation = SortOperation('asc')
        that's will run sort data with ASCENDING
        Sorting selecting row in database
        params :
        1). default is None or operation not permitted
        2). desc is sorting selected data by name by descending
        3). asc  is sorting selected data by name by ascending
     
        sort_choice in params is for get what data will sorted ?
        example, sort_choice = 'salary'
        that's will sorting 'salary' data depening your sort_method params
        params:
        1). default is None and operation not permitted
        2). 'name' is sorting name data
        3). 'salary' is sorting salary data
    '''

    def __init__(self, sort_method, sort_choice):
        self.sort_method = sort_method
        self.sort_choice = sort_choice

    def open_db(self):
        connect = conn()
        return connect

    def close_to_db(self, connector, cursor):
        connector.close()
        cursor.close()
            
    def print_data(self, row_data, showSalaryData=None):
        for data in enumerate(row_data, start=1):
            print(data[0], '-> Name = ', data[1][0])
            if showSalaryData is not None:
                print('     Salary = ', data[1][1])
            print('\n')
    
    def run_sort_data(self):
        if self.sort_method in ('asc', 'desc'):
            
            db_connector = self.open_db()
            db_cursor = db_connector.cursor()
            
            sort_choice = 'get_sort_' + self.sort_choice

            db_cursor.execute(get_sql_statement(sort_choice, None, self.sort_method))
            row_data = db_cursor.fetchall()
            if self.sort_choice == 'salary':
                self.print_data(row_data, showSalaryData=True)
            else:
                self.print_data(row_data)

            self.close_to_db(db_connector, db_cursor)
