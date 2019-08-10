#!/usr/bin/python3
# script that lists all cities from the database hbtn_0e_4_usa


def getStates(userName, passWord, dbName):
    """ Accesses database hbtn_0e_4_usa and grabs cities, then puts in
    ascending order.
    ARGS:
        userName: the username
        passWord: the password
        dbName: the name of the database to access
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
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities LEFT JOIN states "
                "ON cities.state_id = states.id "
                "ORDER BY cities.id ASC;")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    """ Take in arguments and passes to get states from db """
    from sys import argv

    getStates(argv[1], argv[2], argv[3])
