from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import STR_DATABASE

engine = create_engine(STR_DATABASE)

Session = sessionmaker(bind=engine)

# para trabalhar com tabelas
Base = declarative_base()

# cria, caso não existam, as tabelas de todos os modelosque encontrar na aplicação (importados)
def criaTabelas():
    Base.metadata.create_all(engine)

from sqlalchemy import create_engine

engine = create_engine("sqlite:///pastelaria_db.db")
from sqlalchemy import create_engine

engine = create_engine("sqlite:///pastelaria_db.db")
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() 