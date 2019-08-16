#!/usr/bin/python3
# Module containing code for Task 15

if __name__ == "__main__":
    """ creates the State “California” with the City “San Francisco” from
    the database hbtn_0e_100_usa
    """

    from sys import argv
    from sqlalchemy import (create_engine)
    from relationship_state import Base, State
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
