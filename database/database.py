from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

print("#"*100)
print("*"*100)
print("#"*100)

print("\n")
print(f'DB_USER = {os.environ.get("DB_USER")}')
print(f'DB_PASS = {os.environ.get("DB_PASS")}')
print(f'DB_HOST = {os.environ.get("DB_HOST")}')
print(f'DB_NAME = {os.environ.get("DB_NAME")}')
print("\n")

print("#"*100)
print("*"*100)
print("#"*100)


connection_string = URL.create(
    'postgresql',
    username=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASS"),
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("DB_NAME"),
)

engine = create_engine(connection_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
