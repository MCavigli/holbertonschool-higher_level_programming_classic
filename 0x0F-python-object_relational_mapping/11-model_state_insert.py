#!/usr/bin/python3
""" Task 11 """

if __name__ == "__main__":
    """ """

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

    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()
    print(newState.id)
    session.close()
