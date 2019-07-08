def getNameStatement(searchedName):

    sqlSearchStatement = "SELECT id FROM company WHERE name='{searchedName}';"
    
    sqlStatement = sqlSearchStatement.format(searchedName=searchedName)
    
    return sqlStatement


def getAddressStatement(choice, userId):

    updateData = str(input('Enter New Employee Address : '))

    sqlStatement1 = "UPDATE company SET address='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        updateData=updateData, userId=userId)

    return sqlStatement

def getNameStatement(choice, userId):

    updateData = str(input('Enter New Employee Name : '))

    sqlStatement1 = "UPDATE company SET name='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        updateData=updateData, userId=userId)

    return sqlStatement


def getAgeStatement(choice, userId):
    updateData = int(input('Enter New Employee Age: '))

    sqlStatement1 = "UPDATE company SET age='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        updateData=updateData, userId=userId)

    return sqlStatement


def getSalaryStatement(choice, userId):
    updateData = float(input('Enter New Employee Salary : '))

    sqlStatement1 = "UPDATE company SET salary='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        updateData=updateData, userId=userId)

    return sqlStatement
