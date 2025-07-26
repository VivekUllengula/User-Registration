from fastapi import HTTPException

#Exception to find a duplicate user
class DuplicateUser(HTTPException):
    def __init__(self):
        super().__init__(status_code=409, detail="Username already exists.")

#Exception to find a used password
class DuplicateUser(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Password reuse not allowed.")

#Exception to show that password has expired
class DuplicateUser(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Password expired. Please update.")
                
#Exception to show that password reset limit reached
class DuplicateUser(HTTPException):
    def __init__(self):
        super().__init__(status_code=429, detail="Too many reset requests.")
