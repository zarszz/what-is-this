from statement.sqlmainstatement import getAddressStatement, getAgeStatement, getNameStatement, getSalaryStatement

def getSqlStatement(choice, userId):
    if(choice == 'address'):
        sqlStatement = getAddressStatement(choice, userId)
        return sqlStatement
    if(choice == 'age'):
        sqlStatement = getAgeStatement(choice, userId)
        return sqlStatement
    if(choice == 'name'):
        sqlStatement = getNameStatement(choice, userId)
        return sqlStatement
    if(choice == 'salary'):
        sqlStatement = getSalaryStatement(choice, userId)
        return sqlStatement
