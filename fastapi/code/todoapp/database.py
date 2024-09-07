import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if os.getenv("DB") == "POSTGRES":
    if os.getenv("CONTAINER") == "True":
        SQLALCHEMY_DATABASE_URL = \
            'postgresql://postgres:test123@host.docker.internal/TodoApplicationDatabase'
    else:
        SQLALCHEMY_DATABASE_URL = \
            'postgresql://postgres:test123@localhost/TodoApplicationDatabase'
else:
    SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'


# Postgres
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLITE
#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()