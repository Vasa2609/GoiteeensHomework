import os
from sqlalchemy import create_engine
from sqlalchemy.orm import session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv


load_dotenv()
print(os.getenv('DATABASE'))
database = create_engine("sqlite:///database.db", connect_args={'check_same_thread': False})
Session = sessionmaker(bind=database)
session = Session()
BASE = declarative_base()


def create_db():
    BASE.metadata.create_all(database)



def drop_db():
    BASE.metadata.drop_all(database)