from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#Entidad
class Users(BaseModel):
    name: str
    lastname: str
    age: int

user_db = [Users(name="Agustin", lastname="Di Giambatista", age=29),
            Users(name="Matias", lastname="Spule", age=19)]

@app.get("/user")
async def user():
    return user_db