import psycopg2
import os


def conn():
    try:
        conn = psycopg2.connect(host=os.getenv('DBHOST'),
                                database=os.getenv('DBNAME'),
                                user=os.getenv('USERNAME'),
                                password=os.getenv('DBPASSWD'))
        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def testconnector():
    connection = conn()
    print('DATABASE CONNECTED ......')
    db_cursor = connection.cursor()
    db_cursor.execute('SELECT version();')
    db_version = db_cursor.fetchone()
    print(db_version[0])
