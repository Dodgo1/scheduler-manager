import datetime
from typing import List, Literal
from pydantic import BaseModel,Field

class Entry(BaseModel):
    id:str
    user: str
    creation_time: datetime.datetime
    entry_type: int
    weekday: Literal['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    time_start: datetime.time
    time_end: datetime.time
    note: str | None


class DashboardWeekInDB(BaseModel):
    id:str = Field(alias="_id")
    hash: str
    url_token: str
    owner: str
    name: str
    extra_info: str
    entries: List[Entry]


class DashboardWeekInput(BaseModel):
    name: str
    extra_info: str


class DashboardWeekOutput(BaseModel):
    id:str = Field(alias="_id")
    url_token: str
    owner: str
    name: str
    extra_info: str
    entries: List[Entry]


class UserInDB(BaseModel):
    id:str = Field(alias="_id")
    username: str
    password: str
    api_key: str


class UserInput(BaseModel):
    username: str
    password: str


class UserOutput(BaseModel):
    id:str
    username:str
    api_key:str

class NoResponse(BaseModel):
    pass
