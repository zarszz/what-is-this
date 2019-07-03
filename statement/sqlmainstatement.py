def getNameSqlStatement(searchedName):
    sqlSearchStatement = "SELECT id FROM company WHERE name='{searchedName}';".format(
        searchedName=searchedName)
    return sqlSearchStatement


def getAddressStatement(choice, userId):

    updateData = str(input('Enter New Employee Address : '))

    sqlStatement1 = "UPDATE company SET address='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        choice=choice, updateData=updateData, userId=userId)

    return sqlStatement

def getNameStatement(choice, userId):

    updateData = str(input('Enter New Employee Name : '))

    sqlStatement1 = "UPDATE company SET name='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        choice=choice, updateData=updateData, userId=userId)

    return sqlStatement


def getAgeStatement(choice, userId):
    updateData = int(input('Enter New Employee Age: '))

    sqlStatement1 = "UPDATE company SET age='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        choice=choice, updateData=updateData, userId=userId)

    return sqlStatement


def getSalaryStatement(choice, userId):
    updateData = float(input('Enter New Employee Salary : '))

    sqlStatement1 = "UPDATE company SET salary='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        choice=choice, updateData=updateData, userId=userId)

    return sqlStatement
