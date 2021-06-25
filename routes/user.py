from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User, UpdateUser
import redis
import json
from datetime import timedelta


#creating a redis client
client = redis.Redis(host='localhost', port=6379, db=0)

user = APIRouter()


#@user=APIRouter()
@user.get("/get-all-data")
def read_data():
    #here users is table name
    r=client.get('getalldata')
    if r is None:
        print("hitting api")
        r= conn.execute(users.select()).fetchall()
        client.set('getalldata',str(r))
        client.expire('getalldata',timedelta(seconds=60))
        return r
    else:
        print('cache')
        return r
    

@user.get("/get-by-id/{id}")
def read_data(id:int):
    data_key = str(f"{id}_data")
    r=client.get(data_key)
    if r is None:
        print("hitting api")
        r=conn.execute(users.select().where(users.c.id==id)).fetchall()
        client.set(data_key,str(r))
        client.expire(data_key,timedelta(seconds=8400))
        return r
    else:
        print('cache')
        return r
    
    

@user.post("/write-data")
#User is basemodel
def write_data(user:User):
    conn.execute(users.insert().values(
        id =user.id,
        name=user.name,
        email=user.email,
        password = user.password
    ))
    return conn.execute(users.select()).fetchall()

@user.put("/update-data/{id}")
def update_data(id: int, user:UpdateUser):
    query = users.update().\
        where(users.c.id == user.id).\
        values(
            id =user.id,
            name=user.name,
            email=user.email,
            password = user.password
        )
    conn.execute(query)
    # try:
    #     conn.execute(users.update(
    # #         id =user.id,
    # #         name=user.name,
    # #         email=user.email,
    # #         password = user.password
    # #     ).where(users.c.id==id))
    # #     conn.commit()
    # # except Exception as e:
    # #     print(e)
    return conn.execute(users.select()).fetchall()


@user.delete("/delete-data/{id}")
def delete_data(id:int):
    conn.execute(users.delete().where(users.c.id==id))
   
    #here users is table name
    return conn.execute(users.select()).fetchall()

