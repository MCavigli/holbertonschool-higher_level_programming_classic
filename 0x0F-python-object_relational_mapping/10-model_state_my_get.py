#!/usr/bin/python3
""" Task 10 """

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

    my_query = session.query(State).filter(State.name == argv[4])\
                                   .first()
    if my_query:
        print("{}".format(my_query.id))
    else:
        print("Not found")
    '''
    flag = 0
    for state in session.query(State).order_by(State.id).all():
        if state.name == argv[4]:
            flag = 1
            print("{}".format(state.id))
    if flag == 0:
        print("Not found")
    '''
    session.close()
