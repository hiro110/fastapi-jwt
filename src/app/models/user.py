# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP, text
from sqlalchemy.sql.functions import current_timestamp
from pydantic import BaseModel

from db import Base, ENGINE

class UserTable(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(255), unique=True, nullable=False)
    email = Column('email', String(255), unique=True, nullable=False)
    password = Column('password', String(255), nullable=False)
    token = Column('token', TEXT, nullable=True)
    created_at=Column('created_at', TIMESTAMP, server_default=current_timestamp())
    updated_at=Column('updated_at', TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, name, age):
        self.name = name
        self.email = email
        self.password = password
        self.token = token
        now = datetime.now()
        self.created_at = now
        self.updated_at = now


def main():
    # create table
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
