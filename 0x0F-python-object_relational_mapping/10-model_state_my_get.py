#!/usr/bin/python3
""" Module that holds code for Task 10 """

if __name__ == "__main__":
    """
    prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa
    """

    from sys import argv
    from sqlalchemy import (create_engine)
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    my_query = session.query(State).filter(State.name == argv[4])\
                                   .first()
    if my_query:
        print("{}".format(my_query.id))
    else:
        print("Not found")

    session.close()
