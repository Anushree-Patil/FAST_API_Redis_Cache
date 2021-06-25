from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String,BigInteger
from config.db import meta,engine

#build table 'users', here table is a class
users = Table(
    'userss',meta,
    Column('id',Integer,primary_key=True,autoincrement=True),
    Column('name',String(255)),
    Column('email',String(255)),
    Column('password',String(255)),

)

# Create the table in the database
meta.create_all(engine)