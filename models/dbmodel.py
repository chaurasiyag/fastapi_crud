from pydantic import BaseModel, EmailStr

class User(BaseModel):
    user_name:str
    name:str
    email:EmailStr
    password:str
