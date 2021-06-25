from sqlalchemy import create_engine, MetaData


#making connection to the database test
engine =create_engine("mysql+pymysql://root@localhost:3307/test")

#metadata-It is used when reflecting and creating databases in Python (using SQLAlchemy package).
#MetaData is a container object that keeps together many different features of a database (or multiple databases) being described.
meta = MetaData()
conn = engine.connect()