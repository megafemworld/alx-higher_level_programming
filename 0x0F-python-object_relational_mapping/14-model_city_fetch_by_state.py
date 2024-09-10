#!/usr/bin/python3
"""Print all city"""

from sys import sys
from model_city import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(City, State)\
            .filter(City.state_id == state.id).all()
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
