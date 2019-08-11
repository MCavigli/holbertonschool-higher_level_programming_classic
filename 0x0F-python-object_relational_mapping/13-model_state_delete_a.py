#!/usr/bin/python3
# Module containing code for Task 13

if __name__ == "__main__":
    """ deletes all State objects with a name containing the
    letter a from the database hbtn_0e_6_usa
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
        if 'a' in state.name or 'A' in state.name:
            session.delete(state)
    session.commit()
    session.close()
