from fastapi import APIRouter

from config.config import conn
from models.dbmodel import User

from schemas.schemas import userEntity,usersEntity
from bson import ObjectId
user=APIRouter()

@user.get('/')
async def find_all_users():
    print(conn.local.user.find())
    print(usersEntity(conn.local.user.find()))
    return usersEntity( conn.local.user.find())

@user.post('/')
async def create_user(item:User):
    conn.local.user.insert_one(dict(item))
    return usersEntity( conn.local.user.find())

@user.put('/{id}')
async def update_user(id,user:User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return userEntity( conn.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id):
    return "Successfully deleted the  object"+str(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))
    