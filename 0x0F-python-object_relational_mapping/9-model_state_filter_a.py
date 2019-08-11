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

    for state in session.query(State).order_by(State.id).all():
        for char in range(len(state.name)):
            if state.name[char] == 'a':
                print("{}: {}".format(state.id, state.name))
                break
    session.close()