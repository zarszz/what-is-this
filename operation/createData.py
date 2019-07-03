import psycopg2
from operation.connector import conn as connector


def createDataToDB(rownumber):
    pegawai_id = None
    try:
        conn = connector()
        dbCursor = conn.cursor()
        namaPegawai = str(input("masukkan nama pegawai : "))
        umurPegawai = str(input("masukkan umur pegawai : "))
        alamatPegawai = str(input("masukkan alamat gepawai : "))
        gajiPegawai = float(input("masukkan gaji peagawi :"))
        pegawai_db_id = rownumber + 1

        sql = "INSERT INTO company (ID,NAME,AGE,ADDRESS,SALARY) VALUES({pegawai_db_id}, '{namaPegawai}', {umurPegawai}, '{alamatPegawai}', {gajiPegawai}) RETURNING id;"
        sqlQuery = sql.format(pegawai_db_id=str(pegawai_db_id), namaPegawai=namaPegawai,
                              umurPegawai=umurPegawai, alamatPegawai=alamatPegawai, gajiPegawai=str(gajiPegawai))

        dbCursor.execute(sqlQuery)
        conn.commit()
        dbCursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
        print("INSERT DATA SUKSES ......")
