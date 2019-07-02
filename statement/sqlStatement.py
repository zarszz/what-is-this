from statement.sqlmainstatement import *

def getSqlStatement(pilihan, userId):
    if(pilihan == 'alamat'):
        sqlStatement = getAlamatStatement(pilihan, userId)
        return sqlStatement
    if(pilihan == 'umur'):
        sqlStatement = getUmurStatement(pilihan, userId)
        return sqlStatement
    if(pilihan == 'nama'):
        sqlStatement = getNamaStatement(pilihan, userId)
        return sqlStatement
    if(pilihan == 'gaji'):
        sqlStatement = getGajiStatement(pilihan, userId)
        return sqlStatement
