#!/usr/bin/python3
# takes in an argument and displays all values in the states table of
# hbtn_0e_0_usa where name matches the argument
# But this time, it is safe from SQL injections


def getStates(userName, passWord, dbName, stateName):
    """ Accesses database hbtn_0e_0_usa and grabs states that begin with 'N'.
    ARGS:
        userName: the username
        passWord: the password
        dbName: the name of the database to access
        stateName: the name of the state to check
    """

    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=userName,
        passwd=passWord,
        db=dbName,
        charset="utf8"
    )

    cur = db.cursor()
    sqlCommand = "SELECT * FROM states WHERE name = %s;"
    cur.execute(sqlCommand, (stateName,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    """ Take in arguments and passes to get states from db """
    from sys import argv

    getStates(argv[1], argv[2], argv[3], argv[4])
