from pydantic import BaseModel
from typing import Optional
from datetime import date

class UserCreate(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    dob: date
    doj: date
    address: str
    comment: Optional[str] = ""
    active: bool = True
