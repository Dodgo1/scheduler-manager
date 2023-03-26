import os
from dotenv import load_dotenv
import pymongo
from urllib import parse
from models import *
import datetime
from functions import *


class Database:
    def __init__(self):
        load_dotenv()
        mongo_client = pymongo.MongoClient(
            f"mongodb+srv://test1:{parse.quote_plus(os.environ['MONGO_PASSWORD'])}@cluster0.3gozvno.mongodb.net/?retryWrites=true&w=majority")
        db = mongo_client['scheduler-db']
        self.dashboards_coll = db['dashboards']
        self.users_coll = db['users']



    def create_user(self,user:UserInput) -> dict:
        user = dict(user)
        user['password'] = hash_string(user['password'])
        user['api_key'] = hash_string(
            user['username'] + datetime.datetime.now().__str__() + get_random_string(5)
        )
        user['id'] = str(self.users_coll.insert_one(user).inserted_id)
        return user

    def get_user_by_key(self, api_key: str) -> dict:
        return self.users_coll.find_one(
            {"api_key": api_key})

    def get_user(self, username: str, password: str) -> dict:
        user =  self.users_coll.find_one(
            {"username": username, "password": hash_string(password)})
        user["id"] = str(user.pop('_id'))
        return user
    def get_user_by_key(self,api_key):
        return self.users_coll.find_one({"api_key":api_key})
