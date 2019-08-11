#!/usr/bin/python3
# Module containing code for Task 14

if __name__ == "__main__":
    """ prints all City objects from the database hbtn_0e_14_usa """

    from sys import argv
    from sqlalchemy import (create_engine)
    from model_state import Base, State
    from model_city import Base, City
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id)\
                              .all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
