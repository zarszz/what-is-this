def getNameSqlStatement(namaYangDicari):
    sqlSearchStatement = "SELECT id FROM company WHERE name='{namaYangDicari}';".format(
        namaYangDicari=namaYangDicari)
    return sqlSearchStatement


def getAlamatStatement(pilihan, userId):

    updateData = str(input('masukkan alamat yang baru : '))

    sqlStatement1 = "UPDATE company SET address='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        pilihan=pilihan, updateData=updateData, userId=userId)

    return sqlStatement

def getNamaStatement(pilihan, userId):

    updateData = str(input('masukkan nama yang baru : '))

    sqlStatement1 = "UPDATE company SET name='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        pilihan=pilihan, updateData=updateData, userId=userId)

    return sqlStatement


def getUmurStatement(pilihan, userId):
    updateData = int(input('masukkan umur yang baru : '))

    sqlStatement1 = "UPDATE company SET age='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        pilihan=pilihan, updateData=updateData, userId=userId)

    return sqlStatement


def getGajiStatement(pilihan, userId):
    updateData = float(input('masukkan gaji yang baru : '))

    sqlStatement1 = "UPDATE company SET salary='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        pilihan=pilihan, updateData=updateData, userId=userId)

    return sqlStatement
