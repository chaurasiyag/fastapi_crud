def userEntity(item)->dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "password":item["password"],
        "user name":item["user_name"]

    }
def usersEntity(item)->list:
    return [userEntity(user) for user in item]
     