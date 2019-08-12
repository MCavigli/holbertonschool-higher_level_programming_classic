#!/usr/bin/python3
# Module containing code for Task 15

if __name__ == "__main__":
    """ creates the State “California” with the City “San Francisco” from
    the database hbtn_0e_100_usa
    """

    from sys import argv
    from sqlalchemy import (create_engine)
    from relationship_state import State, Base
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newCity = City(name='San Francisco')
    newState = State(name='California', cities=[City(name='San Francisco')])
    session.add(newState)
    session.commit()
    session.close()
