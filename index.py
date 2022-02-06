from fastapi import FastAPI
from route.user import user

app=FastAPI()

app.include_router(user)