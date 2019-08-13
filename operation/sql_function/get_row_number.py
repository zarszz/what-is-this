from operation.connector import conn
from statement.sqlStatement import(
        getSqlStatement as get_sql_statement)

def get_total_row_number():
    """
    "
    "   Get sum of row number in table
    "   return integer()
    "
    """
    connector = conn()
    db_cursor = connector.cursor()
    db_cursor.execute(get_sql_statement('get_row_number'))
    return int(db_cursor.rowcount)
