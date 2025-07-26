from fastapi import APIRouter, Request, HTTPException
from app.models.schemas import UserCreate
from app.core.database import users_collection
from app.core.utils import hash_password, now
from app.core.auth import create_access_token, decode_access_token
from app.core.decorators import log_execution_time
from app.logger import app_logger
from app.core.exceptions import *
from datetime import datetime, time

router = APIRouter()

password_reset_requets = {}

def convert_dates(user_dict: dict) -> dict:
    for key, value in user_dict.items():
        if isinstance(value, datetime.date) and not isinstance(value, datetime.datetime):
            user_dict[key] = datetime.combine(value, time.min)
    return user_dict

#Route to Register or Create a User
@router.post("/register")
@log_execution_time
def register(user: UserCreate):
    if users_collection.find_one({"username": user.username}):
        raise DuplicateUser()
    user_dict = user.dict()
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    user_dict["password_history"] = [user_dict["password"]]
    user_dict["last_password_change"] = now()
    users_collection.insert_one(user_dict)
    app_logger.info(f"User registered: {user.username}")
    return{"message": "User registered successfully"}
    
