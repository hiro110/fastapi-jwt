import os
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

user_name = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
host = os.environ.get('MYSQL_SERVER')
database_name = os.environ.get('MYSQL_DB')

DATABASE = ''
if 'mysql.database.azure.com' in host:
    DATABASE = sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        username=user_name,
        password=password,
        host=host,
        port=3306,
        database=database_name,
        query={"ssl_ca": "/home/site/wwwroot/src/DigiCertGlobalRootCA.crt.pem"},
    )
else:
    DATABASE = sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        username=user_name,
        password=password,
        host=host,
        port=3306,
        database=database_name,
    )

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()
