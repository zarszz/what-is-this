from statement.sqlmainstatement import *

def getSqlStatement(choice, userId):
    choice = str(choice)
    if(choice.lower == 'address'):
        sqlStatement = getAddressStatement(choice, userId)
        return sqlStatement
    if(choice.lower == 'age'):
        sqlStatement = getAgeStatement(choice, userId)
        return sqlStatement
    if(choice.lower == 'name'):
        sqlStatement = getNameStatement(choice, userId)
        return sqlStatement
    if(choice.lower == 'salary'):
        sqlStatement = getSalaryStatement(choice, userId)
        return sqlStatement
