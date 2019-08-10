#!/usr/bin/python3
#  takes in the name of a state as an argument and lists all cities
# of that state, using the database hbtn_0e_4_usa


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

    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON states.id = cities.state_id "
                "WHERE states.name = %s;", (stateName,))
    query_rows = cur.fetchall()
    '''
    query_rows = [i[0] for i in query_rows]
    queryLen = len(query_rows)
    j = 0
    for row in query_rows:
        if j == queryLen - 1:
            print("{}".format(row))
        else:
            print("{}".format(row), end=", ")
            j += 1
    '''
    print(", ".join([i[0] for i in query_rows]))
    cur.close()
    db.close()

if __name__ == "__main__":
    """ Take in arguments and passes to get states from db """
    from sys import argv

    getStates(argv[1], argv[2], argv[3], argv[4])
