import psycopg2
import os


def conn():
    try:
      conn = psycopg2.connect(host="localhost", database=os.getenv('DBNAME'),
                              user=os.getenv('USERNAME'), password='')
      dbCursor = conn.cursor()
      print('DATABASE CONNECTED ......')

      print('postgreSQL version : ',end='')
      dbCursor.execute('SELECT version()')
      db_ver = dbCursor.fetchone()
      print(db_ver)

      return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == "__main__":
    conn()
