#!/usr/bin/python3
# Module with code for Task 9

if __name__ == "__main__":
    """  lists all State objects that contain the letter a from the database
    hbtn_0e_6_usa
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

    letterA = session.query(State).filter(State.name.like("%a%"))
    for state in letterA:
        print("{}: {}".format(state.id, state.name))
    session.close()
