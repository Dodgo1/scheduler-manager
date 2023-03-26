from fastapi import FastAPI,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer
from database import Database
from models import *
from http import HTTPStatus


app = FastAPI()
db = Database()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def check_api_key(api_key:str = Depends(oauth2_scheme)):
    if not db.get_user_by_key(api_key):
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Invalid api key"
        )

@app.get("/")
async def get_api_status():
    return {"status": "active"}

@app.post("/user",response_model=NoResponse,status_code=HTTPStatus.CREATED)
async def create_user(username:str,password:str):
    if db.get_user(username,password) is not None:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail="Username is taken"
        )

@app.get("/user",status_code=HTTPStatus.OK,response_model=UserOutput)
async def get_user(username:str,password:str):
    return db.get_user(username,password)

