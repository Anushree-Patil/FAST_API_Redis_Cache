from pydantic import BaseModel
from typing import Optional

class Config:
        orm_mode = True


#Define the base schema for working with API request and response
class User(BaseModel):
        id:int
        name:str
        email:str
        password:str

class UpdateUser(BaseModel):
        id:Optional[int]=None
        name:Optional[str]=None
        email:Optional[str]=None
        password:Optional[str]=None